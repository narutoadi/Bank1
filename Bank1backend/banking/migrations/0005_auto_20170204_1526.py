# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0004_auto_20170204_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountNumber',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
    ]
