# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_auto_20161128_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
