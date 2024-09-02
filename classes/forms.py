from django import forms
from .models import Classes


class Classes_RegistrationForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = "__all__"