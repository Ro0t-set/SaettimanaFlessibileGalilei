# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_corso_max_iscritti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corso',
            name='max_iscritti',
        ),
        migrations.RemoveField(
            model_name='corso',
            name='studenti',
        ),
        migrations.AddField(
            model_name='aula',
            name='max_iscritti',
            field=models.IntegerField(default=0),
        ),
    ]