from django import forms
from .models import Student

class StudentForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()