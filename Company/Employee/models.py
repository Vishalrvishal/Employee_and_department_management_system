from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name=models.CharField(max_length=50,default=None)
    employee_age=models.IntegerField(default=None)
    employee_address=models.CharField(max_length=100,default=None)
    employee_department=models.CharField(max_length=30,default=None)
    employee_reporting_manager=models.CharField(max_length=50,default=None)
    employee_email=models.EmailField(max_length=50,unique=True)