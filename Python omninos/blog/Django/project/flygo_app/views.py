from django.shortcuts import render,redirect
from.models import Flights
from.forms import flight_form
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def Booking(request,id=0):
    if request.method=='GET':
        if id==0:
            form=flight_form()
        else:
            data=Flights.objects.get(pk=id)
            form=flight_form(instance=data)
        return render(request,"booking.html",{"form":form})
    else:
        if id==0:
            form=flight_form(request.POST)
        else:
            data=Flights.objects.get(pk=id)
            form=flight_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("list")
    
def list(request):
    list=Flights.objects.all()
    return render(request,"list.html",{"list":list})
def data_delete(request,id):
    data=Flights.objects.get(pk=id)
    data.delete()
    return redirect("list")
def Home(request):
    return render(request,"home.html",)
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login (request,user)
            return redirect("booking")
        else:
            messages.info(request,"Invalid username / password ")
            return redirect("login")
        

    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
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

