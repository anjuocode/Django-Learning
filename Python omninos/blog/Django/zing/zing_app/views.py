from django.shortcuts import render
from.forms import zing_form
from.models import Zing
# Create your views here.
def home(request):
    if request.method=="GET":
        form=zing_form()
    else:
        form=zing_form(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"form.html",{"form":form})
def list(request):
    list=Zing.objects.all()
    return render(request,"list.html",{"list":list})