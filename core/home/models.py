from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100)

#Book with category model
class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Book(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)

#Vehicle with a Car model
class Car(models.Model):
    car_name = models.CharField(max_length=100)

class Vehicle(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    vehile_title = models.CharField(max_length=100)

