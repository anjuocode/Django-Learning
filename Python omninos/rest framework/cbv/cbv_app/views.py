
from django.shortcuts import render
from.serializers import stu_serializer
from.models import Student
from rest_framework.response import Response
from rest_framework import status,serializers
from rest_framework.views import APIView
from django.http.response import Http404
# Create your views here.

class student_list(APIView):
    def get(self):
        student=Student.objects.all()
        serializer=stu_serializer(student,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=stu_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class stu_detail(APIView):
    def get_object(self,id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        student=self.get_object(id)
        serializer=stu_serializer(student)
        return Response(serializer.data)
    def put(self,request,id):
        student=self.get_object(id)
        serializer=stu_serializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        student=self.get_object(id)

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    

