from django import forms
from .models import Student


class Student_RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"