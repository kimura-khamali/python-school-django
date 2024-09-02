from django.shortcuts import render

# Create your views here.
from class_period.forms import Class_Period_RegistrationForm




def class_period_register_view(request):
    form = Class_Period_RegistrationForm()
    return render(request, 'class_period/class_period_register_view.html', {"form": form})


