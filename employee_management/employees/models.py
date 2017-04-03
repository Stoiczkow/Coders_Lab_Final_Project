from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    @property
    def name(self):
        return "{} {}".format(self.last_name, self.first_name)

    def __str__(self):
        return self.name


class Stand(models.Model):
    name = models.CharField(max_length=64)


