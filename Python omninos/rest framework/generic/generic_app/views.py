from operator import ge
from django.shortcuts import render
from.models import Student
from.serializers import stu_serialzer
from rest_framework import generics
# Create your views here.
class student_list(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=stu_serialzer
class stu_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=stu_serialzer
