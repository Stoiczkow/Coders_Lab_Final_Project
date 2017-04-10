from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from .validators import valid_date

# Create your models here.
class Stand(models.Model):
    name = models.CharField(max_length=64)

    @property
    def stand_name(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.stand_name


class Employee(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="Imię")
    last_name = models.CharField(max_length=64, verbose_name="Nazwisko")
    basic_salary = models.FloatField(verbose_name="Płaca podstawowa",  validators = [MinValueValidator(0.0)])
    is_available = models.BooleanField(default=True)

    @property
    def name(self):
        return "{} {}".format(self.last_name, self.first_name)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("employees")

def avalible_employees():
    employees = Employee.objects.filter(basic_salary=2000)
    employees_choices = {}
    for employee in employees:
        employees_choices['id']=str(employee.last_name)

class Task(models.Model):
    title = models.CharField(max_length=256, verbose_name="Nazwa")
    stand = models.ForeignKey(Stand, verbose_name="Stanowisko")
    start_date = models.DateField(verbose_name="Początek zlecenia")
    end_date = models.DateField(verbose_name="Koniec zlecenia")
    employees = models.ManyToManyField(Employee, verbose_name="Pracownicy", blank=True, limit_choices_to={'is_available': 'True'})
    is_active = models.BooleanField(default=True)
    target = models.IntegerField(verbose_name="Cel")
    accomplishment = models.IntegerField(default=0, verbose_name="Wykonanie")
    is_closed = models.BooleanField(default=False, verbose_name="Zamknij zlecenie")
    is_taken = models.BooleanField(default=False, verbose_name="Zajmij zlecenie")

    def get_absolute_url(self):
        return reverse("all_tasks")