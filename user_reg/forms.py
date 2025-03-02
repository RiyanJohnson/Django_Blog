from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #keeps the configuration in one place and saves it to the User model
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']
