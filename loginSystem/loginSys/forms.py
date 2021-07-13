from django import forms


class registerForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)


class loginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())

    username.widget.attrs.update({
        'class': 'form-control',
        'name': 'username',
        'id': 'formGroupExampleInput',
        'placeholder': 'Username'
    })