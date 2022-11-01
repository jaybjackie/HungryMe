from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(
                                max_length=30,
                                required= True,
                                help_text='Enter the username',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username*'}))

    password1 = forms.CharField(
                                help_text='Enter Password',
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password*'}))
    password2 = forms.CharField(
                                help_text='Repeat Password',
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password*'}))
                              
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']