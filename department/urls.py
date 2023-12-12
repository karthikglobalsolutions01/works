from department.views import *
from django.urls import path,include
urlpatterns=[
    path('Department/', DepartmentuList.as_view(), name='grade_list'),
    path('Department/<int:pk>', DepartmentuupdateDetails.as_view(), name='gradeupdate'),
]