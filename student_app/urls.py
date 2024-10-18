from django.urls import path
from .views import Studentcreateview, Studentdetailview

urlpatterns = [
    path('students/', Studentcreateview.as_view(), name ='student-list-create'),
    path('students/<int:pk>/', Studentdetailview.as_view(), name='student-detail'),
]