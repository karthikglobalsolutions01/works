from rest_framework import serializers

class PDFFormSerializer(serializers.Serializer):
    pdf_file = serializers.FileField()
