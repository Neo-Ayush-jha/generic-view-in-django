from django import forms
from .models import *
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentRecord
        fields ="__all__"