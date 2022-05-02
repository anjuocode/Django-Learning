import re
from django.shortcuts import redirect, render
from .models import Blog
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken")
                return redirect("register")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1)
                user.save()
                messages.info(request,"username created")
                return redirect(login )
        else:
            messages.info(request,"password did not match")
            return redirect("register")
    else:
        return render(request,"register.html")
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid username/password")
            return redirect("login")
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect("/")
def blog(request):
    base=Blog.objects.all()
    if register.method=="POST":
        search=request.POST['search']
        result=Blog.objects.filter(title_contains=search)
        return render(request,"base.html",{"base":result})
    else:
        return render(request,"base.html",{"base":base})