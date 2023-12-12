from Designation.views import *
from django.urls import path,include
urlpatterns=[
    path('Designation/', DesignationList.as_view(), name='designation_list'),
    path('Designation/<int:pk>', DesignationupdateDetails.as_view(), name='designationupdate'),
]