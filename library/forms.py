from django.contrib.auth.models import User
from django import forms
from django.forms import DateInput


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class BookIssueForm(forms.Form):
    return_date = forms.DateField(required=True, widget=DateInput(attrs={'type': 'date'}))
    email = forms.EmailField()
    address = forms.CharField()
    phone = forms.CharField()


class ProfileUpdateForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
