from email import message
from email.policy import default
from django.shortcuts import redirect, render
import requests
import datetime
from django.contrib import messages
# Create your views here.
def home(request):
    city=request.POST.get('city','mohali') 
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3000d65db45783f0e7948b5bd47316f7"
    data=requests.get(url).json()

    if data['cod']=='404':
        messages.info(request,"Enter valid city name")
        return redirect('home')
    elif city is "":
        url="https://api.openweathermap.org/data/2.5/weather?q=mohali&appid=3000d65db45783f0e7948b5bd47316f7"
    
    else:
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3000d65db45783f0e7948b5bd47316f7"
    data=requests.get(url).json()
    minutes=30
    hours=5
    current_time=datetime.datetime.now()
    hour_add=datetime.timedelta(hours=hours,minutes=minutes)
    time=current_time + hour_add
    payload = {
        'name': data['name'],
        'weather': data['weather'][0]['main'],
        'country':data['sys']['country'],
        'icon':data['weather'][0]['icon'],
        'kel_far':int(((data['main']['temp']) - 273) * 9/5 + 32),
        'far_cel':int(data['main']['temp']) - 273,
        'humidity':data['main']['humidity'],
        'pressure':data['main']['pressure'],
        'wind':data['wind']['speed'],
        't':time
    }


    context = {'data':payload}

    return render(request,"home.html",context)