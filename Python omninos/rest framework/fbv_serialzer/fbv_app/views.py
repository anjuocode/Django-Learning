from turtle import st
from urllib import response
from django.shortcuts import render
from.models import Student
from.serializer import stu_serializer
from rest_framework.response import Response
from rest_framework import status,serializers
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def student_list(request):
    if request.method=="GET":
        student=Student.objects.all()
        serializer=stu_serializer(student,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=stu_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def student_detail(request,Id):
    try:
        student=Student.objects.get(Id=Id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=stu_serializer(student)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=stu_serializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


