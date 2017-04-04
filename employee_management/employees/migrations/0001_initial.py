# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('basic_salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Nazwa')),
                ('start_date', models.DateField(verbose_name='Początek zlecenia')),
                ('end_date', models.DateField(verbose_name='Koniec zlecenia')),
                ('employees', models.ManyToManyField(to='employees.Employee', verbose_name='Pracownicy')),
            ],
        ),
    ]
