from django import forms
from django.shortcuts import redirect, render
from.forms import emp_form
from.models import Employee
# Create your views here.
def base(request,id=0):
    if request.method=="GET":
        if id==0:
            form=emp_form()
        else:
            data=Employee.objects.get(pk=id)
            form=emp_form(instance=data)
        return render(request,"form.html",{"form":form})
    else:
        if id==0:
            form=emp_form(request.POST)
        else:
            data=Employee.objects.get(pk=id)
            form=emp_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
    return redirect("list")

def list(request):
    list=Employee.objects.all()
    return render(request,"list.html",{"list":list})
def data_del(request,id):
    data=Employee.objects.get(pk=id)
    data.delete()
    return redirect("list")

    
def index(request):

    return render(request,"base.html")