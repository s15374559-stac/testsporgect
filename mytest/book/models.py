from django.db import models
# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pubish_year= models.IntegerField()



class Student(models.Model):
    name =models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    age= models.IntegerField()   


