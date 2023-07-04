from django import forms
from django.contrib.auth.forms import AuthenticationForm
from . import models
import re

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label="First Name", 
                                widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, label="Last Name",
                               widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    teamname = forms.CharField(max_length=250, label="Username", 
                              widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    affiliation = forms.CharField(max_length=500, required=False, label="affiliation", 
                              widget=forms.TextInput(attrs={'placeholder': 'Affiliation - Choose what best represents you'}))
    email = forms.EmailField(max_length=250, label="Email", 
                             widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Email'}))
    password = forms.CharField(max_length=250, min_length=8, label="Password", 
                               widget=forms.TextInput(attrs={'type':'password', 'placeholder': 'Password'}))
    
    def clean_teamname(self):
        teamname = self.cleaned_data['teamname']
        if teamname:
            # Convert to lowercase
            teamname = teamname.lower()

            # Minimum length of 6 and maximum length of 20
            if len(teamname) < 6 or len(teamname) > 20:
                raise forms.ValidationError("Username must be between 6 and 20 characters.")

            # Valid characters: letters (a-z), numbers (0-9), and periods (.)
            if not re.match(r'^[a-zA-Z0-9.]+$', teamname):
                raise forms.ValidationError("Username can only contain letters, numbers, and periods.")
            
            if '..' in teamname:
                raise forms.ValidationError("Username cannot contain more than one period in a row.")

            # Team name cannot start or end with special characters
            if not teamname[0].isalnum() or not teamname[-1].isalnum():
                raise forms.ValidationError("Username cannot start or end with special characters.")

            # Check if the team name is already taken
            if models.Teams.objects.filter(teamname=teamname).exists():
                raise forms.ValidationError("Username already taken.")

            return teamname

    class Meta:
        model = models.Teams
        fields = ["first_name", "last_name", "teamname", "affiliation", "email"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label="Username", 
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=250, min_length=8, label="Password", 
                               widget=forms.TextInput(attrs={'type':'password', 'placeholder': 'Password'}))


class AffiliationForm(forms.ModelForm):
    class Meta:
        model = models.Teams
        fields = ['affiliation']

