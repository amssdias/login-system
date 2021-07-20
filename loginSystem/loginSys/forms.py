from django import forms
from .models import MyUser

class registerForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class loginForm(forms.Form):
    username = forms.CharField(label="Username", required=False)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

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


    def clean(self):
        cleaned_data    = super().clean()
        username        = cleaned_data.get("username")
        password        = cleaned_data.get("password")

        if not len(username):
            raise forms.ValidationError("You should provide some username")
        elif not len(password):
            raise forms.ValidationError("You should provide some password")