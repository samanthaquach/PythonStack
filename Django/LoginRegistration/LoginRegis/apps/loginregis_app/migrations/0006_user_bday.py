# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-18 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginregis_app', '0005_auto_20171018_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bday',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
