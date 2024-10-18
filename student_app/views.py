from django.shortcuts import render
from .models import studentmodel
from .serializers import Studentserilaizer
from rest_framework import generics, status
from rest_framework.response import Response

class Studentcreateview(generics.ListCreateAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = Studentserilaizer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
         serializer = self.get_serializer(data=request.data, many=True)
         serializer.is_valid(raise_exception=True)
         self.perform_create(serializer)
         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Optionally handle single entry if needed
        return super().create(request, *args, **kwargs)

class Studentdetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = studentmodel.objects.all()
    serializer_class = Studentserilaizer    
