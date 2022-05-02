from django import forms
from.models import Library


class library_form(forms.ModelForm):
    class Meta:
        model=Library
        fields="__all__"


        widgets={
            "stu_name":forms.TextInput(attrs={"placeholder":"enter passenger name"}),
            
            "issue_date":forms.TextInput(attrs={"placeholder":"Where want to go from "}),
            "return_date":forms.TextInput(attrs={"placeholder":"destination"})
        }
