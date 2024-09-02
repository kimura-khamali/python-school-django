from django import forms
from .models import Class_Period


class Class_Period_RegistrationForm(forms.ModelForm):
    class Meta:
        model = Class_Period
        fields = "__all__"