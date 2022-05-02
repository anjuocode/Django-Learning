from dataclasses import field
from django import forms 
from.models import Flights
class DateInput(forms.DateInput):
    input_type='date'
class flight_form(forms.ModelForm):
    class Meta:
        model=Flights
        fields="__all__"
    
        widgets={
            'Name':forms.TextInput(attrs={"placeholder":'Enter your Name'}),
            'Mobile':forms.TextInput(attrs={"placeholder":'mobile number'}),
            "From":forms.TextInput(attrs={'placeholder':'Enter city or airport'}),
            'To':forms.TextInput(attrs={"placeholder":'Enter city ofr airport'}),
            'Departure':DateInput(),
            'Return':DateInput()
 }