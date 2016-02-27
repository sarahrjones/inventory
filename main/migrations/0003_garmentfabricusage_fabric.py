# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151214_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='garmentfabricusage',
            name='fabric',
            field=models.ForeignKey(to='main.Fabric', null=True),
        ),
    ]
