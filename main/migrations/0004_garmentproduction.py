# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_garmentfabricusage_fabric'),
    ]

    operations = [
        migrations.CreateModel(
            name='GarmentProduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('garments_made', models.IntegerField(default=0)),
                ('garment', models.ForeignKey(to='main.Garment', null=True)),
            ],
        ),
    ]
