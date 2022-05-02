from django.shortcuts import redirect, render
from .models import XYZ
from .forms import xyz_form

# Create your views here.
def base(request,id=0):
    if request.method=="GET":
        if id==0:
            form=xyz_form()
        else:
            emp=XYZ.objects.get(pk=id)
            form=xyz_form(instance=emp)
        return render(request,"form.html",{"form":form})

    else:
        if id==0:
          form=xyz_form(request.POST)
        else:
            emp=XYZ.objects.get(pk=id)
            form=xyz_form(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect("list")


def list(request):
    list=XYZ.objects.all()
    return render(request,"list.html",{"list":list})


def xyz_del(request,id):
    list=XYZ.objects.get(pk=id)
    list.delete()
    return redirect("list")