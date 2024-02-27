from django.urls import path
from .views import *

urlpatterns = [
    path("student/",StudentAPI.as_view()),
    path("register/",RegisterUser.as_view()),
]
