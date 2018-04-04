# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_placelist_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeannotation',
            name='place',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='lists.Place'),
            preserve_default=False,
        ),
    ]
