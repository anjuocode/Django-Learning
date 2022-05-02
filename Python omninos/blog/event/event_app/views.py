from django.shortcuts import render,redirect
from .models import Contact_us, Culture, Family
from.models import Business
from.models import Charity
from.models import Bookevent
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        message=request.POST.get('message')
        if ((name and mobile and email and message)==''):
            messages.info(request,"Invalid form")
        else:
            contacts=Contact_us(Name=name,Mobile=mobile,Email=email,Message=message)
            contacts.save()
            messages.info(request,"message has been sent")
            return redirect("/")
    return render(request,"home.html")
def family(request):
    family=Family.objects.all()
    return render(request,"family.html",{"family":family})
def culture(request):
    culture=Culture.objects.all()
    return render(request,"culture.html",{"culture":culture})
def charity(request):
    charity=Charity.objects.all()
    return render(request,"charity.html",{"charity":charity})
def business(request):
    business=Business.objects.all()
    return render(request,"business.html",{"business":business})
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
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login (request,user)
            return redirect("book")
        else:
            messages.info(request,"Invalid username / password ")
            return redirect("login")
        

    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
@login_required(login_url="login")
def book(request):
    if request.method=="POST":
        Name = request.POST['name']
        Mobile = request.POST['mobile']
        Location = request.POST['location']
        Email = request.POST['email']
        People = request.POST['people']
        Date = request.POST['date']
        Event = request.POST['event']
        Food = request.POST['food']
        Address = request.POST['address']
        Message = request.POST['message']
        if ((Mobile and Email and Address )==''):
            messages.info(request,'warning field  must be taken')
            return redirect('book')
        else:
            guest = Bookevent( Name=Name,Mobile=Mobile,Location=Location, Email=Email,People=People,Date=Date,Event=Event,Food=Food,Address= Address,Message=Message)
            guest.user=request.user
            guest.Name=request.user
            guest.save()
            messages.info(request,'Booking has been successfully')
            return redirect('book')
    return render(request,'bookevent.html')
    
def user_cart(request):
    my_cart=Bookevent.objects.filter(user=request.user)
    return render(request,"user_cart.html",{"my_cart":my_cart})
def base(request):


    return render(request,"base.html")
def contact_us(request):
    return render(request,"contact_us.html")



   

