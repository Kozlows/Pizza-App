from django import forms
from .models import *

class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ["username", "password"]