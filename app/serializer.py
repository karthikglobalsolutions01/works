from rest_framework import serializers

class PDFFormSerializer(serializers.Serializer):
    pdf_file = serializers.FileField()
    CSTIN=serializers.CharField(max_length=100)
    GSTIN=serializers.CharField(max_length=100)
    State_Code=serializers.CharField(max_length=100)
    Invoice_Number=serializers.CharField(max_length=100)
    
