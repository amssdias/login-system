from django import forms
from .models import MyUser
    

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
        first_name              = self.cleaned_data.get("first_name") or ''
        last_name               = self.cleaned_data.get("last_name") or ''
        username                = self.cleaned_data.get("username") or ''
        password                = self.cleaned_data.get("password") or ''
        password_confirmation   = self.cleaned_data.get("password_confirmation") or ''
        email                   = self.cleaned_data.get("email") or ''

        if not len(first_name) or not len(last_name):
            raise forms.ValidationError("You should provide first and last name!")
        if not len(username):
            raise forms.ValidationError("You should provide some username!")
        if not len(password) or not len(password_confirmation) or len(password) < 8:
            raise forms.ValidationError("Password must be 8 characters minimum")
        if not len(email):
            raise forms.ValidationError("You should provide some email!")
        if password != password_confirmation:
            raise forms.ValidationError("Passwords don't match!")


    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        return first_name.capitalize()
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        return last_name.capitalize()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@gmail.com' not in email:
            raise forms.ValidationError("Email must be 'gmail'.")
        return email


class LoginForm(forms.Form):
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