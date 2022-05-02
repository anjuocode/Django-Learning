# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from.models import Library
from.forms import library_form
# Create your views here.
def base(request,stu_id=0):
    if request.method=="GET":
        if stu_id==0:
            form=library_form()
        else:
            data=Library.objects.get(pk=stu_id)
            form=library_form(instance=data)
        return render(request,"form.html",{"form":form})
    else:
        if id==0:
            form=library_form(request.POST)
        else:
            data=Library.objects.get(pk=stu_id)
            form=library_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
    return redirect("list")

def List(request):
    show=Library.objects.all()
    return render(request,"list.html",{"list":show})
def data_del(request,stu_id):
    data=Library.objects.get(pk=stu_id)
    data.delete()
    return redirect("list")

def index(request):

    return render(request,"base.html")