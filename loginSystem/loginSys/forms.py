from django import forms
from .models import MyUser


class registerForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class loginForm(forms.Form):
    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

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