# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-11 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_banktransactions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BankTransactions',
            new_name='BankTransaction',
        ),
    ]