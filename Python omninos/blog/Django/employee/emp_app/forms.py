from django import forms
from django.forms import fields, widgets
from.models import Employee 
class emp_form(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"


        labels={ 
            "name":"NAME",
            "salary":"SALARY",
            "position":"POSITION"
        }
        widgets={
            "name":forms.TextInput(attrs={'placeholder':'enter the name'}),
            'salary':forms.TextInput(attrs={"placeholder":'enter the salary'}),
             
        }
        
    def __init__(self,*args,**kwargs):
        super(emp_form,self).__init__(*args, **kwargs)
        self.fields["position"].empty_label='Select'
        self.fields["name"].required=True
        self.fields["salary"].required=True
    

