from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage

from django.contrib.auth.decorators import login_required

from .models import MyUser
from .forms import LoginForm, RegisterForm
from .utils import generate_token


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

            # Activate account
            current_site = get_current_site(request)
            email_subject = "Activate your account"
            message = render_to_string("activate_email/activate.html", 
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": generate_token.make_token(user)
            })

            email = EmailMessage(
                subject=email_subject,
                body=message,
                to=[user.email],
            )

            email.send()
            
            # Send message saying user got registered sucessfully
            message = "User registered successfully, check your email to activate your account!"
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

            return redirect('login')

        return render(request, "activate_email/failed_activation.html", status=401)


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
