from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *



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

class CreateFoodFrom(forms.ModelForm):
    menuname = forms.CharField(
                                max_length=50,
                                required= True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'must be less than or equal to 50 letters'}))
    
    description = forms.CharField(
                                max_length=250,
                                required= True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'must be less than or equal to 250 letters'}))
    
    ingredients = forms.CharField(
                                max_length=250,
                                required= True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name'}))
    
    picture_url = forms.URLField(
                                required= True,
                                widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder':'Picture URL'}))
    
    totalcal = forms.FloatField(
                                required= True,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Calories'}))
    
    fatcalorie = forms.FloatField(
                                required= True,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Calories'}))
    
    sugar = forms.FloatField(
                                required= True,
                                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Calories'}))
    
    difficulty = forms.ChoiceField(
                                required= True,
                                widget=forms.RadioSelect(attrs={'class': 'form-control', 'placeholder':''}))
    
    
    
    class Meta:
        model = CookBook
        fields = ['menuname','description','ingredients','picture_url','totalcal','fatcalorie','sugar','difficulty']