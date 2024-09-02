from django import forms
from .models import Teacher


class Teacher_RegistrationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"