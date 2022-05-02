from django import forms
from.models import Redbus


class redbus_form(forms.ModelForm):
    class Meta:
        model=Redbus
        fields="__all__"


        widgets={
            "passenger_name":forms.TextInput(attrs={"placeholder":"enter passenger name"}),
            "passenger_id":forms.TextInput(attrs={"placeholder":"enter passenger id"}),
            "where":forms.TextInput(attrs={"placeholder":"Where want to go from "}),
            "to":forms.TextInput(attrs={"placeholder":"destination"})
        }
