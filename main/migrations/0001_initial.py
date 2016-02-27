# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FabricStockInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mill', models.CharField(max_length=100)),
                ('quality', models.CharField(max_length=100)),
                ('color_code', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('yards', models.FloatField()),
                ('fabric', models.ForeignKey(to='main.Fabric')),
            ],
        ),
        migrations.CreateModel(
            name='Garment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('style', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GarmentFabricUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yards_used', models.FloatField()),
                ('fabric', models.ForeignKey(to='main.Fabric')),
            ],
        ),
    ]
