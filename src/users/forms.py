from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

        
class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'firstname',
            'lastname',
            'username',
            'email',
            'password1',
            'password2'
        ]

    firstname = forms.CharField()
    lastname = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()