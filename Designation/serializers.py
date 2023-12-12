from rest_framework import serializers
from .models import designation
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=designation
        fields='__all__'