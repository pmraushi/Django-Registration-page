from django import forms


class NameForm(forms.Form):
    first_name = forms.CharField(label='Your First name', max_length=100)
    last_name = forms.CharField(label='Your Last name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')


class LoginForm(forms.Form):
    # email = forms.EmailField()
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
