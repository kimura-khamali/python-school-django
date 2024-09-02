from django.shortcuts import render

# Create your views here.


from teacher.forms import Teacher_RegistrationForm


def teacher_register_view(request):
    form = Teacher_RegistrationForm()
    return render(request, 'teachers/teacher_register_view.html', {"form": form})
