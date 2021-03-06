# Generated by Django 2.0.3 on 2018-04-03 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0005_auto_20180403_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placelist',
            name='followers',
        ),
        migrations.AddField(
            model_name='placelist',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscribed_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listupdate',
            name='update_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='updates', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='places', to='cities.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='place',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='places', to='lists.PlaceType'),
        ),
        migrations.AlterField(
            model_name='placeannotation',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='place_annotations', to='lists.Placelist'),
        ),
        migrations.AlterField(
            model_name='placelist',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lists', to='cities.City'),
        ),
        migrations.RemoveField(
            model_name='placelist',
            name='collaborators',
        ),
        migrations.AddField(
            model_name='placelist',
            name='collaborators',
            field=models.ManyToManyField(blank=True, null=True, related_name='collaborates_on', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='placelist',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lists', to='cities.Neighborhood'),
        ),
        migrations.AlterField(
            model_name='placelist',
            name='places',
            field=models.ManyToManyField(blank=True, related_name='included_in', to='lists.Place'),
        ),
        migrations.AlterField(
            model_name='placelist',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lists', to='lists.ListType'),
        ),
        migrations.AlterField(
            model_name='placetype',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtypes', to='lists.PlaceType'),
        ),
    ]
