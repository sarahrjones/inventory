# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-21 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_garmentproduction_fabric'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fabricstockinfo',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='fabricstockinfo',
            name='width',
        ),
        migrations.AddField(
            model_name='fabric',
            name='weight_oz',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='fabric',
            name='width_in',
            field=models.IntegerField(default=0),
        ),
    ]
