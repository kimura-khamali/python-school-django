# from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login ,logout 
# from django.contrib import messages

# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            redirect('home')
            # return '/student/'

        else:
            messages.error(request, 'invalid username or password') 
    return render(request, 'accounts/login.html')           


def user_logout(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'accounts/home.html')