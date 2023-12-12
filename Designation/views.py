from django.shortcuts import render
from Designation.serializers import DesignationSerializer
from Designation.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
class DesignationList(ListCreateAPIView):
    queryset = designation.objects.all()
    serializer_class = DesignationSerializer

class DesignationupdateDetails(RetrieveUpdateDestroyAPIView):
    queryset = designation.objects.all()
    serializer_class = DesignationSerializer
# Create your views here.
