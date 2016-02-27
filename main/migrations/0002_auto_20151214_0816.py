# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garmentfabricusage',
            name='fabric',
        ),
        migrations.AddField(
            model_name='garmentfabricusage',
            name='garment',
            field=models.ForeignKey(to='main.Garment', null=True),
        ),
        migrations.AlterField(
            model_name='garment',
            name='description',
            field=models.CharField(default=b'description', max_length=100),
        ),
        migrations.AlterField(
            model_name='garment',
            name='style',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
