from django.db import models

# Create your models here.
class Pdf_Info_Table(models.Model):
    Invoice_Number=models.IntegerField(primary_key=True)
    CSTIN=models.CharField(max_length=100)
    GSTIN=models.CharField(max_length=100)
    State_Code=models.CharField(max_length=100)
    Invoice_Amount=models.CharField(max_length=100,null=True,blank=True)
    
    
