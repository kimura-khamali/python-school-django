from django.shortcuts import render

# Create your views here.



from student.forms import Student_RegistrationForm



def courses_register_view(request):
    form = Student_RegistrationForm()
    return render(request, 'courses/courses_register_view.html', {"form": form})


