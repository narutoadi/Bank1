# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_auto_20170203_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountNumber',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
