# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-04 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='stand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employees.Stand'),
            preserve_default=False,
        ),
    ]