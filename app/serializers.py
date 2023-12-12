from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,ReadOnlyField
from .models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.ReadOnlyField(source='dept.department')
    designation =serializers.ReadOnlyField(source='desig.Designation')

    class Meta:
        model=Employee
        fields='__all__'
        