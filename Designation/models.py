from django.db import models

# Create your models here.
class designation(models.Model):
    designation_id =models.IntegerField(primary_key=True)
    Designation=models.CharField(max_length=100)
    