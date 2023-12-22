from django.db import models

# Create your models here.
class Pdf_Info_Table(models.Model):
    Invoice_Number=models.CharField(max_length=100,unique=True)
    CSTIN=models.CharField(max_length=100,null=True,blank=True)
    GSTIN=models.CharField(max_length=100,null=True,blank=True)
    State_Code=models.CharField(max_length=1000,null=True,blank=True)
    
    
