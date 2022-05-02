from django.shortcuts import render,redirect
from.forms import rav_form
from.models import Rav
# Create your views here.
def base(request,id=0):
    if request.method=="GET":
        if id==0:
            form=rav_form()
        else:
            data=Rav.objects.get(pk=id)
            form=rav_form(instance=data)
        return render(request,"form.html",{"form":form})

            
    else:
        if id==0:
            form=rav_form(request.POST)
        else:
            data=Rav.objects.get(pk=id)
            form=rav_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect("list")

    
def list(request):
    list=Rav.objects.all()
    return render(request,"list.html",{"list":list})
def data_del(request,id):
    data=Rav.objects.get(pk=id)
    data.delete()
    return redirect("list")