from django import forms
from django.forms import fields 
from .models import Rav

class rav_form(forms.ModelForm):
    class Meta:
        model=Rav
        fields="__all__"