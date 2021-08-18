from django.contrib.auth.forms import PasswordResetForm
from django.core import validators
from django.core.validators import EmailValidator
from django import forms
from .models import MyUser
from .validators import validate_password, validate_domain_email


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
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), validators=[validate_password])
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), validators=[validate_domain_email])

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        cleaned_data            = super().clean()
        password                = self.cleaned_data.get("password")
        password_confirmation   = self.cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Passwords don't match!", code='password_mismatch')
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
        email_name = email.split("@")
        if len(email_name[0]) < 2:
            raise forms.ValidationError("Email must be valid. (At least 2 characters)", code='Invalid email name.')
        return email


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


class UpdatePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])
    password_1 = forms.CharField(label="Password confirmation" ,widget=forms.PasswordInput())

    password.widget.attrs.update({
        'class': 'form-control',
        'name': 'password',
        'placeholder': 'Password'
    })
    
    password_1.widget.attrs.update({
        'class': 'form-control',
        'name': 'password_1',
        'placeholder': 'Password confirmation'
    })

    class Meta:
        model = MyUser
        fields = ['password']

    def save(self, commit=True):
        self.instance.set_password(self.instance.password)
        if commit:
            self.instance.save()
            self._save_m2m()
        return self.instance

    def clean(self):
        cleaned_data            = super().clean()
        password                = self.cleaned_data.get("password")
        password_1              = self.cleaned_data.get("password_1")

        if password and password_1 and password != password_1:
            raise forms.ValidationError("Passwords don't match!", code='password_mismatch')
        return self.cleaned_data