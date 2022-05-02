from django.shortcuts import redirect, render
from.forms import company_form
from.models import Company
# Create your views here.
def base(request,id=0):
    if request.method=="GET":
        if id==0:
            form=company_form()
        else:
            data=Company.objects.get(pk=id)
            form=company_form(instance=data)
        return render(request,"form.html",{"form":form})

    else:
        if id==0:
            form=company_form(request.POST)
        else:
            data=Company.objects.get(pk=id)
            form=company_form(instance=data)
        if form.is_valid():
            form.save()
    return redirect("list")
    
def list(request):
    list=Company.objects.all()
    return render(request,"list.html",{"list":list})