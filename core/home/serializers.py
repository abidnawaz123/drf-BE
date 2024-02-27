from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    def create( self, validate_data):
        user = User.objects.create(username = validate_data["username"])
        user.set_password(validate_data["password"])
        user.save()
        return user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, data):
        if data["age"] < 18:
            raise serializers.ValidationError({"error" : "age must be greater or equal to 18"})
        if data["name"]:
            for x in data["name"]:
                if x.isdigit():
                    raise serializers.ValidationError({"error" : "name cannot contains numbers"})
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
        depth = 1

