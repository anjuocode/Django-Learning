from django.db.models.query import RawQuerySet
from django.shortcuts import render,redirect
from.models import Blog
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request," email already taken")
                return redirect("register")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save() 
                messages.info(request,"username created")
                return redirect("login")  
        else:
            messages.info(request,"password did not match")
            return redirect("register")     
    else:
         return render(request,"register.html")



def base(request):
    Blog_all=Blog.objects.all()
    if request.method=="POST":
        search=request.POST["search"]
        result=Blog.objects.filter(blog_heading__contains=search)
        return render(request,"base.html",{"form":result})
    else:
        return render(request,"base.html",{"form":Blog_all})


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login (request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid username / password ")
            return redirect("login")
        

    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def treks(request):
    return render(request,"tracking.html")
def parag(request):
    return render(request,"paragliding.html")
