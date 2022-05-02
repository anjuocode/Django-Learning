from django import forms
from django.db import models
from django.db.models import fields 
from.models import Practice

class forms(forms.ModelForm):
    class Meta:
        model=Practice
        fields="__all__"