from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return HttpResponse('this is my first web page without html file')
def Xyz(request):
    return HttpResponse("this is my exercise content")
def practice(request):
    return HttpResponse("this is third exercise content")
def hello(request):
    return HttpResponse("Hello, How are you")
def hello1(request):
    return HttpResponse("In publishing and graphic design,Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content.")
def hello2(request):
    return HttpResponse('<h1 style="color:red;">hii</h1>')
                                 