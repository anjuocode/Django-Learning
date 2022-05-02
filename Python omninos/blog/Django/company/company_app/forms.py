from django import forms
from django.forms import fields 
from.models import Company
class company_form(forms.ModelForm):
    class Meta:
        model=Company
        fields="__all__"