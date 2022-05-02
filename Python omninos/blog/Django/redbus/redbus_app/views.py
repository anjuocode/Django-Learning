from django.shortcuts import redirect, render
from.forms import redbus_form
from.models import Redbus
# Create your views here.
def base(request,id=0):
    if request.method=="GET":
        if id==0:
            form=redbus_form()
        else:
            data=Redbus.objects.get(pk=id)
            form=redbus_form(instance=data)
        return render(request,"form.html",{"form":form})
    else:
        if id==0:
            form=redbus_form(request.POST)
        else:
            data=Redbus.objects.get(pk=id)
            form=redbus_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
    return redirect("list")

def list(request):
    list=Redbus.objects.all()
    return render(request,"list.html",{"list":list})
def data_del(request,id):
    data=Redbus.objects.get(pk=id)
    data.delete()
    return redirect("list")

def index(request):

    return render(request,"base.html")