from django.contrib.auth.forms import PasswordResetForm
from django.core import validators
from django.core.validators import EmailValidator
from django import forms
from .models import MyUser


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'form-control',
            'placeholder': 'email'
            })
    )


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        cleaned_data            = super().clean()
        password                = self.cleaned_data.get("password")
        password_confirmation   = self.cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Passwords don't match!", code='Invalid password confirmation.')
        return self.cleaned_data

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("You should provide a first name!", code='No first name.')
        return first_name.capitalize()
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name:
            raise forms.ValidationError("You should provide a last name!", code='No last name.')
        return last_name.capitalize()
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("Must have a username.", code="No username.") 
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "gmail.com" not in email:
            raise forms.ValidationError("Email must be gmail.")
        email_name = email.split("@")
        if len(email_name) < 2:
            raise forms.ValidationError("Email must be valid. (At least 2 characters)", code='Invalid email name.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("Password must be 8 characters minimum", code='Invalid password length.')
        return password


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())

    username.widget.attrs.update({
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Username'
    })

    password.widget.attrs.update({
        'class': 'form-control',
        'name': 'password',
        'placeholder': 'Password'
    })

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("You should provide some username")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("You should provide some password")
        return password