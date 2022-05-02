from django.shortcuts import render
from .forms import student_forms
from.models import student

# Create your views here.
def base(request):
    if request.method=='GET':
    
        form=student_forms()
    else:
        form=student_forms(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'student_form.html',{'anju':form})


def data_show(request):
    show=student.objects.all()
    return render(request,'list.html',{"show":show})