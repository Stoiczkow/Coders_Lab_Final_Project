from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    basic_salary = models.FloatField()

    @property
    def name(self):
        return "{} {}".format(self.last_name, self.first_name)

    def __str__(self):
        return self.name


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

    def get_absolute_url(self):
        return reverse("add_task")