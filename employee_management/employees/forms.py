from django import forms
from .models import Stand, Employee, Task
from django.db.models.functions import Concat
from django.db.models import Value

employees_choices = Employee.objects.filter(pk=3).values_list('id', 'last_name')
class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)

