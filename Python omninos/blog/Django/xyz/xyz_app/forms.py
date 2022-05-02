from django import forms
from django.forms import fields 
from .models import XYZ 
class xyz_form (forms.ModelForm):
    class Meta:
        model=XYZ
        fields="__all__"