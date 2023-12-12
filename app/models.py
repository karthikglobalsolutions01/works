from django.db import models
from department.models import *
from Designation.models import *
class Employee(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    id=models.IntegerField(primary_key=True)
    contact=models.IntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    dept = models.ForeignKey(departmentu, on_delete=models.SET_NULL, blank=True, null=True)
    desig = models.ForeignKey(designation, on_delete=models.SET_NULL, blank=True, null=True)
    resume=models.FileField(null=True,blank=True)
def __str__(self) -> str:
        return self.name
    
    
