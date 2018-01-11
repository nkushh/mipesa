# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-11 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=200)),
                ('account_name', models.CharField(max_length=200)),
                ('account_no', models.CharField(max_length=20)),
                ('balance', models.FloatField(default=0)),
                ('date_created', models.DateField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]