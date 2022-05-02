from django.shortcuts import render
from .forms import shop_form
from.models import Shop

# Create your views here.
def base(request):
    if request.method=='GET':
    
        form=shop_form()
    else:
        form=shop_form(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'form.html',{'form':form})


def list(request):
    show=Shop.objects.all()
    return render(request,'list.html',{"list":show})