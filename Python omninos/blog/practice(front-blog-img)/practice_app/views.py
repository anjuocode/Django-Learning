from django.shortcuts import redirect, render
from .forms import forms
from .models import Practice
# Create your views here.
def home(request):
    if request.method=="GET":
        form=forms()
        return render(request,"form.html",{"form":form})
    else:
        form=forms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect("/")
    
def data(request):
    data=Practice.objects.all()
    return render(request,"list.html",{"list":data})