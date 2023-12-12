from django.shortcuts import render
from department.serializer import DepartmentuSerializer
from department.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
class DepartmentuList(ListCreateAPIView):
    queryset = departmentu.objects.all()
    serializer_class = DepartmentuSerializer

class DepartmentuupdateDetails(RetrieveUpdateDestroyAPIView):
    queryset = departmentu.objects.all()
    serializer_class = DepartmentuSerializer

# Create your views here.
