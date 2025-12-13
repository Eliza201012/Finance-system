from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, 
                               widget=forms.TextInput(attrs={"class" : "form-control"}))
    email = forms.EmailField(required=True, 
                             widget=forms.EmailInput(attrs={"class" : "form-control"}))
    password1 = forms.CharField(max_length=20, required=True,
                                widget=forms.PasswordInput(attrs={"class" : "form-control"}))
    password2 = forms.CharField(max_length=20, required=True,
                                widget=forms.PasswordInput(attrs={"class" : "form-control"}))
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=100, 
                               widget=forms.TextInput(attrs={"class" : "form-control"}))
    email = forms.EmailField(required=True, 
                             widget=forms.EmailInput(attrs={"class" : "form-control"}))
    
    class Meta:
        model = User
        fields = ("username", "email")

class UpdateProfileForm(forms.ModelForm):
    currency = forms.CharField(max_length=10,
                               widget=forms.TextInput(attrs={"class" : "form-control"}))
    
    class Meta:
        model = Profile
        fields = ("currency", )