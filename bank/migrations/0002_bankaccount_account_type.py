# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-11 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='account_type',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
