from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text, DjangoUnicodeDecodeError

from django.contrib.auth.decorators import login_required

from .models import MyUser
from .forms import LoginForm, RegisterForm
from .utils import generate_token, email_activate_account


def register(request):
    if request.user.is_authenticated:
            return redirect("main")

    register_form = RegisterForm(request.POST or None)

    if request.method == "POST":
        
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(user.password)
            user.is_active = False
            user.save()

            email_activate_account(request, user)
            
            # Send message saying user got registered sucessfully
            messages.info(request, "User registered successfully, check your email to activate your account!")
            return redirect("login")
        else:
            context = {'register_form': register_form}
            return render(request, "loginSys/register.html", context=context, status=400)


    context = {'register_form': register_form}
    return render(request, "loginSys/register.html", context=context)


def activate_account(request, uidb64, token):
    if request.method == "GET":
        try:
            # Get user id and activate account
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = MyUser.objects.get(pk=uid)

        except Exception as identifier:
            user=None
        

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Your account was successfully activated, you can now log in!")
            return redirect('login')

        return render(request, "activate_email/failed_activation.html", status=401)


def _login(request):

    if request.user.is_authenticated:
        return redirect('main')

    login_form = LoginForm(request.POST or None, auto_id="id_for_%s", label_suffix=": ")
    context = {"login_form": login_form}

    if request.method == "POST":

        if login_form.is_valid():
            username    = login_form.cleaned_data.get('username')
            password    = login_form.cleaned_data.get('password')

            try:
                user = MyUser.objects.get(username=username)
                if not user.is_active:
                    email_activate_account(request, user)
                    messages.info(request, "User is not active, check your email for an activation link.")
                    return render(request, "loginSys/login.html", context=context, status=403)
            except:
                messages.error(request, "Username doesn't exist")
                return render(request, "loginSys/login.html", context=context, status=401)

            user        = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                messages.error(request, "Invalid username or password")
                return render(request, "loginSys/login.html", context=context, status=401)

    return render(request, "loginSys/login.html", context=context)


def _logout(request):
    logout(request)
    messages.success(request, "You have logged out, see you later!")
    return redirect("login")


@login_required(login_url="login") # Redirect if not logged in
def main(request):
    return render(request, "loginSys/index.html")

@login_required(login_url="login")
def update_password(request):
    if request.method == "POST":
        new_password = request.POST.get('new_password')
        user = request.user
        user.set_password(new_password)
        user.save()
        messages.success(request, "Password Updated")
        return render(request, "loginSys/index.html")

    return render(request, "update_password/password_update.html")