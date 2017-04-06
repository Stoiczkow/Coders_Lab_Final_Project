from django import forms
from .models import Stand, Employee, Task
from django.db.models.functions import Concat
from django.db.models import Value


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)
