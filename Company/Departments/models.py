from django.db import models

# Create your models here.
class Department(models.Model):
    department_name=models.CharField(max_length=50,default=None)
    department_projects=models.IntegerField(default=None)
    department_head=models.CharField(max_length=30,default=None)
    department_region=models.CharField(max_length=30,default=None)
    