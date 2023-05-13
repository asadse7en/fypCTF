from django import forms
from django.contrib.auth.forms import AuthenticationForm
from . import models

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label="First Name", 
                                widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, label="Last Name",
                               widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    teamname = forms.CharField(max_length=250, label="Team Name", 
                              widget=forms.TextInput(attrs={'placeholder': 'TeamName/UserName'}))
    email = forms.EmailField(max_length=250, label="Email", 
                             widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Email'}))
    password = forms.CharField(max_length=250, min_length=8, label="Password", 
                               widget=forms.TextInput(attrs={'type':'password', 'placeholder': 'Password'}))

    class Meta:
        model = models.Teams
        fields = ["first_name", "last_name", "teamname", "email"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label="Team Name", 
                               widget=forms.TextInput(attrs={'placeholder': 'Team Name'}))
    password = forms.CharField(max_length=250, min_length=8, label="Password", 
                               widget=forms.TextInput(attrs={'type':'password', 'placeholder': 'Password'}))
