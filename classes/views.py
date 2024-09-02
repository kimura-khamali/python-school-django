from django.shortcuts import render


from classes.forms import Classes_RegistrationForm



def classes_register_view(request):
    form = Classes_RegistrationForm()
    return render(request, 'classes/classes_register_view.html', {"form": form})

