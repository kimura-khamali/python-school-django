from django.shortcuts import redirect, render
from student.forms import Student_RegistrationForm

def student_register_view(request):
    if request.method == "POST":
        form = Student_RegistrationForm(request.POST)
        if form.is_valid():  
            form.save()  
            return redirect("student_register_view")  

    else:
        form = Student_RegistrationForm()

    return render(request, 'students/student_register_view.html', {"form": form})

