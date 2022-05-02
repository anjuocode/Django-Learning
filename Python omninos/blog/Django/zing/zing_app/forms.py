from django import forms
from django.forms import fields
from.models import Zing

class zing_form(forms.ModelForm):
    class Meta:
        model=Zing
        fields="__all__"

        labels={
            "name":"NAME",
            "last_name":"LAST NAME",
            "id":"ID",
            "branch":"BRANCH"
    }
        widgets={
            "name":forms.TextInput(attrs={"placeholder":"enter the name"}),
            "last_name":forms.TextInput(attrs={"placeholder":"enter last name"}),
            "id":forms.TextInput(attrs={"placeholder":"enter id"}),
            "branch":forms.TextInput(attrs={"placeholder":"enter branch"})
        }
    def __init__(self,*args,**kwargs):
        super(zing_form,self).__init__(*args,**kwargs)
        self.fields["name"].required=True
        self.fields["last_name"].required=False
        self.fields["id"].required=True
        self.fields["branch"].required=False