# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-21 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160221_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='FabricBolt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yards', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='fabricstockinfo',
            name='yards',
        ),
        migrations.AddField(
            model_name='fabricbolt',
            name='fabric_stock_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.FabricStockInfo'),
        ),
    ]
