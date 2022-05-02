from django import forms
from django.forms import fields 
from.models import Shop
class shop_form(forms.ModelForm):
    class Meta:
        model=Shop
        fields="__all__"
