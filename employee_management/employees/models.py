from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from .validators import valid_date

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="Imię")
    last_name = models.CharField(max_length=64, verbose_name="Nazwisko")
    basic_salary = models.FloatField(verbose_name="Płaca podstawowa",  validators = [MinValueValidator(0.0)])

    @property
    def name(self):
        return "{} {}".format(self.last_name, self.first_name)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("employees")

class Stand(models.Model):
    name = models.CharField(max_length=64)

    @property
    def stand_name(self):
        return "{}".format(self.name)

    def __str__(self):
        return self.stand_name


class Task(models.Model):
    title = models.CharField(max_length=256, verbose_name="Nazwa")
    stand = models.ForeignKey(Stand)
    start_date = models.DateField(verbose_name="Początek zlecenia")
    end_date = models.DateField(verbose_name="Koniec zlecenia")
    employees = models.ManyToManyField(Employee, verbose_name="Pracownicy")
    is_active = models.BooleanField(default=True)
    target = models.IntegerField(verbose_name="Cel")
    accomplishment = models.IntegerField(default=0, verbose_name="Wykonanie")
    is_closed = models.BooleanField(default=False, verbose_name="Zamknij zlecenie")

    def get_absolute_url(self):
        return reverse("all_tasks")