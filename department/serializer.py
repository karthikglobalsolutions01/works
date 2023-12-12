from rest_framework import serializers
from .models import departmentu
class DepartmentuSerializer(serializers.ModelSerializer):
    class Meta:
        model=departmentu
        fields='__all__'
        # fields=['department_id','department_name']
        