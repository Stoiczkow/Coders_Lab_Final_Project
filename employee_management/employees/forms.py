from django import forms
from .models import Stand, Employee
from django.db.models.functions import Concat
from django.db.models import Value

stands = Stand.objects.all().values_list('id', 'name')
employees = Employee.objects.all().values_list('id', 'last_name')
employees = employees.annotate(full_name=Concat('last_name', Value(' '), 'first_name'))
employees_choices = employees.values_list('id', 'full_name')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=256, label="Nazwa")
    stand = forms.ChoiceField(choices=stands, label="Stanowisko")
    start_date = forms.DateField(widget=forms.DateInput, label="Początek zlecenia")
    end_date = forms.DateField(widget=forms.DateInput, label="Koniec zlecenia")
    employees = forms.MultipleChoiceField(choices=employees_choices, label="Pracownicy")
    is_active = forms.ChoiceField(widget=forms.CheckboxInput, label="Zlecenie w trakcie")
