from app.views import *
from django.urls import path,include
urlpatterns=[
    path('Employee/', EmployeeList.as_view(), name='grade_list'),
    path('Employee/<int:pk>', EmployeeupdateDetails.as_view(), name='gradeupdate'),
]