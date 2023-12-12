from django.db import models

# Create your models here.
class departmentu(models.Model):
    department_id=models.IntegerField(primary_key=True)
    department=models.CharField(max_length=100)
    