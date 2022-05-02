from django.shortcuts import redirect, render
from.forms import bus_form
from.models import Bus
# Create your views here.
def base(request,id=0):
    if request.method=="GET":
        if id==0:
            form=bus_form()
        else:
            data=Bus.objects.get(pk=id)
            form=bus_form(instance=data)
        return render(request,"form.html",{"form":form})
    else:
        if id==0:
            form=bus_form(request.POST)
        else:
            data=Bus.objects.get(pk=id)
            form=bus_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
    return redirect("list")

def list(request):
    list=Bus.objects.all()
    return render(request,"list.html",{"list":list})
def data_del(request,id):
    data=Bus.objects.get(pk=id)
    data.delete()
    return redirect("list")

