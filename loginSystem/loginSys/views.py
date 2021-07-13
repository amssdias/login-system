from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import MyUser
from .forms import loginForm


def register(request):
    if request.user.is_authenticated:
            return redirect("main")

    if request.method == "POST":

        username            = request.POST['username']
        first_name          = request.POST['first_name']
        last_name           = request.POST['last_name']
        password            = request.POST['password']
        password_confirm    = request.POST['password_confirm']
        email               = request.POST['email']

        if password != password_confirm:
            pass

        new_user = MyUser(username=username, first_name=first_name,
                          last_name=last_name, password=password, email=email)
        new_user.save()
        message = "User registered successfully"
        # Send message saying user got registered sucessfully
        return redirect("login")

    else:
        return render(request, "loginSys/register.html")


def _login(request):

    if request.user.is_authenticated:
        return redirect('main')

    if request.method == "POST":

        username    = request.POST['username']
        password    = request.POST['password']
        user        = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            return render(request, "loginSys/login.html", context={'error': 'Invalid Password'})

    else:
        return render(request, "loginSys/login.html", context={'loginform': loginForm()})


def _logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login") # Redirect if not logged in
def main(request):
    return render(request, "loginSys/index.html")
