from django import forms
from .models import Courses


class Courses_RegistrationForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"