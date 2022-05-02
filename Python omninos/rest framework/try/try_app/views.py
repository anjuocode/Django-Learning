from os import stat
from django.shortcuts import render
from .serializers import try_ser
from.models import Try
from rest_framework.response import Response
from rest_framework import status,serializers
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def list(request):
    if request.method=="GET":
        xyz=Try.objects.all()
        ser=try_ser(xyz,many=True)
        return Response(ser.data)
    else:
        ser=try_ser(data=request.POST)
        if ser.is_valid():
            ser.save()
        return Response(ser.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def detail(request,id):
    try:
        xyz=Try.objects.get(pk=id)
    except Try.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        ser=try_ser(xyz)
        return Response(ser.data)
    elif request.method=="PUT":
        ser=try_ser(xyz,data=request.POST)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
    elif request.method=="DELETE":
        xyz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
