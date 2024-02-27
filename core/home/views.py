from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializers(data=request.data)
        if not serializer.is_valid():
            return Response({"status":403,"message" : "Something went wrong", "errors" : serializer.errors })
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response(
            {"status":200,
            "payload" : serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            "message" : "Your data is saved successfully" 
            })
    
class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        print(request.user)
        return Response({"status":200, "payload" : serializer.data})
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({"status":403,"message" : "Something went wrong", "errors" : serializer.errors })
        serializer.save()
        return Response({"status":200, "payload" : serializer.data, "message" : "Your data is saved successfully" })
    
    def put(self,request):
        pass

    def patch(self,request):
        try:
            student_obj = Student.objects.get(id=request.data["id"])
            serializer = StudentSerializer(student_obj, data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status': 403,'errors': serializer.errors,'message' : "Cannot update data"})
            serializer.save()
            return Response({'status' : 200, 'payload' : serializer.data, 'message' : "Updated user successfully"})
        
        except Exception as e:
            return Response({"status":403,"message" : "invalid id" })

    def delete(self,request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({"status": 200, "message" : "Deleted User Successfully"})

        except Exception as e:
            print(e)
            raise TypeError({"error" : "undefined user id"})
