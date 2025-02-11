from django import forms
from . import models

class Login(forms.Form):
    username = forms.CharField(label="Your name", max_length=100)
    password = forms.CharField(label="Your password", max_length=100)