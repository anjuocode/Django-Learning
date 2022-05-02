from django.shortcuts import redirect, render
from.models import Project
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here. 
def registration(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken")
                return redirect("form")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already taken")
                return redirect("form")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,"Username created")
                return redirect("login")
        else:
            messages.info(request,"password did not match ")
            return redirect("form")
    else:
        return render(request,"form.html")

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid usernam/password")
            return redirect("login")

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")
def home(request):
    Blog_all=Project.objects.all()
    if request.method=="POST":
        search=request.POST["search"]
        result=Project.objects.filter(heading__contains=search)
        return render(request,"home.html",{"form":result})
    else:
        return render(request,"home.html",{"form":Blog_all})

def rafting(request):
    return render(request,"rafting.html")
def parag(request):
    return render(request,"paraglding.html")
def treking(request):
    return render(request,"treking.html")
def navbar(request):
    return render(request,"navbar.html")