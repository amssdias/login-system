from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.views import View
from django.http import HttpResponseBadRequest

from loginSys.models import MyUser
from loginSys.forms import LoginForm, RegisterForm, UpdatePasswordForm
from loginSys.utils import generate_token, email_activate_account, logger


class RegisterUser(View):
    form_class = RegisterForm
    template_name = "loginSys/register.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("main")

        context = {'register_form': self.form_class}
        return render(request, "loginSys/register.html", context=context)

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.is_active = False
            user.save()

            try:
                email_activate_account(request, user)
            except Exception as e:
                messages.error(request, e)
                context = {'register_form': form}
                return render(request, self.template_name, context=context, status=400)
            logger.info(f'User: {user.username} got registered')
            messages.info(request, "User registered successfully, check your email to activate your account!")
            return redirect("login")
        else:
            context = {'register_form': form}
            return render(request, self.template_name, context=context, status=400)


class ActivateAccount(View):
    template_name = "activate_email/failed_activation.html"
    
    def get(self, request, uidb64, token):
        try:
            # Get user id and activate account
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = MyUser.objects.get(pk=uid)

        except Exception as identifier:
            logger.critical(f'User tryed to activate account but failed.')
            user=None
        
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Your account was successfully activated, you can now log in!")
            return redirect('login')

        return render(request, self.template_name, status=400)


class LoginUser(View):
    form_class = LoginForm
    template_name = "loginSys/login.html"
    context = {}

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main')
        self.context['login_form'] = self.form_class(auto_id="id_for_%s", label_suffix=": ")
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        form = self.form_class(request.POST, auto_id="id_for_%s", label_suffix=": ")
        if form.is_valid():
            username    = form.cleaned_data.get('username')
            password    = form.cleaned_data.get('password')

        try:
            user = MyUser.objects.get(Q(username=username) | Q(email=username)).first()
            if not user.is_active:
                email_activate_account(request, user)
                messages.info(request, "User is not active, check your email for an activation link.")
                return render(request, self.template_name, context=self.context, status=403)
        except MyUser.DoesNotExist:
            messages.error(request, "Username doesn't exist")
            return render(request, self.template_name, context=self.context, status=404)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            logger.info(f'User: {user.username} logged in.')
            login(request, user)
            return redirect("main")
        else:
            messages.error(request, "Invalid username or password")
            return render(request, self.template_name, context=self.context, status=401)


class LogoutUser(View):
    def post(self, request):
        logger.info(f'User: {request.user.username} logged out.')
        logout(request)
        messages.success(request, "You have logged out, see you later!")
        return redirect("login")


class MainView(View):
    def get(self, request):
        return render(request, "loginSys/index.html")


class UpdatePassword(LoginRequiredMixin ,View):
    login_url = '/auth/login/'
    form_class = UpdatePasswordForm
    template_name = "update_password/password_update.html"

    def get(self, request):
        context = {'update_password_form': self.form_class}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form_class(request.POST or None, instance=request.user)

        if form.is_valid():
            form.save()

            # Prevent logging out user session
            update_session_auth_hash(request, request.user)
            messages.success(request, "Password Updated")
            return redirect("main")
        else:
            context = {'update_password_form': form}
            return render(request, self.template_name, context=context)

