
# Create your views here.
from django.shortcuts import render,redirect
from .forms import sipro_form
from .models import Sipro
# Create your views here.
def base(request,id=0):
    if request.method=="GET":
        if id==0:
            form=sipro_form()
        else:
            data=Sipro.objects.get(pk=id)
            form=sipro_form(instance=data)
        return render(request, "form.html", {"form": form})
    else:
        if id==0:
            form=sipro_form(request.POST)
        else:
            data=Sipro.objects.get(pk=id)
            form=sipro_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return redirect('list')



def list(request):
    list=Sipro.objects.all()
    return render(request,"list.html",{"list":list})




def data_del(request,id):
    data=Sipro.objects.get(pk=id)
    data.delete()
    return redirect('list')


