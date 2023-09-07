from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    eno=models.IntegerField()
    email=models.EmailField()
    esal=models.FloatField()