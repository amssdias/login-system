from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import MyUser
from .forms import LoginForm, RegisterForm


def register(request):
    if request.user.is_authenticated:
            return redirect("main")

    register_form = RegisterForm()

    if request.method == "POST":

        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()

            message = "User registered successfully, we have sent an email to confirm!"
            # Send message saying user got registered sucessfully
            return redirect("login")
        else:
            context = {'register_form': register_form}
            return render(request, "loginSys/register.html", context=context, status=400)


    context = {'register_form': register_form}
    return render(request, "loginSys/register.html", context=context)


def _login(request):

    if request.user.is_authenticated:
        return redirect('main')

    login_form = LoginForm(auto_id="id_for_%s", label_suffix=": ")

    if request.method == "POST":

        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            username    = login_form.cleaned_data.get('username')
            password    = login_form.cleaned_data.get('password')
            user        = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                context = {
                    'login_form': login_form,
                    'error_authentication': "Invalid username or password"
                    }
                return render(request, "loginSys/login.html", context=context, status=401)

    context = {"login_form": login_form}
    return render(request, "loginSys/login.html", context=context)


def _logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login") # Redirect if not logged in
def main(request):
    return render(request, "loginSys/index.html")
