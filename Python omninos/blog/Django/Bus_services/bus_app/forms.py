from django import forms 
from.models import Bus
class bus_form(forms.ModelForm):
    class Meta:
        model=Bus
        fields="__all__"
