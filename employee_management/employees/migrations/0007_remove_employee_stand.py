# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-06 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20170406_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='stand',
        ),
    ]
