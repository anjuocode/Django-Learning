from django import forms
from django import forms
from.models import student
class student_forms(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"
        