# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_placelist_google_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placelist',
            name='google_id',
        ),
        migrations.AddField(
            model_name='place',
            name='google_id',
            field=models.CharField(default='', max_length=75),
        ),
    ]
