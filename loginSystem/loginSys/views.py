from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import MyUser
from .forms import loginForm, registerForm


def register(request):
    if request.user.is_authenticated:
            return redirect("main")

    register_form = registerForm()
    context = {'register_form': register_form}

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
        return render(request, "loginSys/register.html", context=context)


def _login(request):

    if request.user.is_authenticated:
        return redirect('main')

    login_form = loginForm(auto_id="id_for_%s", label_suffix=": ")
    context = {"login_form": login_form}

    if request.method == "POST":

        login_form = loginForm(request.POST)

        if login_form.is_valid():

            username    = login_form.cleaned_data.get('username')
            password    = login_form.cleaned_data.get('password')
            user        = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                context['error'] = "Invalid username or password"
                return render(request, "loginSys/login.html", context=context, status=401)

    else:
        return render(request, "loginSys/login.html", context=context)


def _logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login") # Redirect if not logged in
def main(request):
    return render(request, "loginSys/index.html")
