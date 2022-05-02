from django.shortcuts import render
from.models import Student
from.serializers import stu_serializer
from rest_framework import generics,mixins
# Create your views here.
class stu_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=stu_serializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class stu_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=stu_serializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)
    