# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 03:19
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ListUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_type', models.CharField(choices=[('add', 'Add Places'), ('remove', 'Remove Places')], max_length=10)),
                ('update_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='name')),
                ('zip_code', models.CharField(max_length=5, null=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='cities.City')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='cities.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Placelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('multi_city', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='title')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists_created', to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='cities.City')),
                ('collaborators', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collaborates_on', to=settings.AUTH_USER_MODEL)),
                ('followers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following_lists', to=settings.AUTH_USER_MODEL)),
                ('neighborhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='cities.Neighborhood')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='lists.ListType')),
            ],
        ),
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtypes', to='lists.PlaceType')),
            ],
        ),
        migrations.AddField(
            model_name='placeannotation',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_annotations', to='lists.Placelist'),
        ),
        migrations.AddField(
            model_name='place',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='lists.PlaceType'),
        ),
        migrations.AddField(
            model_name='listupdate',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='lists.Placelist'),
        ),
        migrations.AddField(
            model_name='listupdate',
            name='update_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updates', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='listtype',
            name='place_types',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_list_types', to='lists.PlaceType'),
        ),
        migrations.AlterUniqueTogether(
            name='placelist',
            unique_together=set([('slug', 'author')]),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together=set([('slug', 'city')]),
        ),
    ]
