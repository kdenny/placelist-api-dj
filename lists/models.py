# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cities.models import City, Neighborhood
from django.contrib.auth.models import User
from autoslug import AutoSlugField


# Create your models here.

class PlaceType(models.Model):
    name = models.CharField(max_length=100)
    parent_type = models.ForeignKey("self", blank=True, null=True, related_name='subtypes', on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class ListType(models.Model):
    name = models.CharField(max_length=100)
    place_types = models.ManyToManyField(PlaceType, blank=True, null=True, related_name='related_list_types')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Place(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=100)
    type = models.ForeignKey(PlaceType, related_name='places', null=True, on_delete=models.SET_NULL)

    city = models.ForeignKey(City, related_name='places', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, related_name='places', on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=250)
    url = models.CharField(max_length=100, null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(max_length=255, populate_from='name')
    google_id = models.CharField(max_length=75, default='')


    zip_code = models.CharField(max_length=5, null=True)

    lat = models.FloatField()
    lon = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    # point = models.PointField()

    class Meta:
        unique_together = ('slug', 'city')

    # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

    def __str__(self):
        return self.name + " - " + self.neighborhood.name + ", " + self.city.name


class Placelist(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    title = models.CharField(max_length=100)
    type = models.ForeignKey(ListType, related_name='lists', on_delete=models.SET_NULL, null=True)
    places = models.ManyToManyField(Place, related_name='included_in', blank=True)
    description = models.TextField(blank=True, null=True)

    city = models.ForeignKey(City, related_name='lists', blank=True, null=True, on_delete=models.SET_NULL)
    neighborhood = models.ForeignKey(Neighborhood, related_name='lists', blank=True, null=True, on_delete=models.SET_NULL)
    multi_city = models.BooleanField(default=False)

    author = models.ForeignKey(User, related_name='lists_created', on_delete=models.CASCADE)
    collaborators = models.ManyToManyField(User, blank=True, null=True, related_name='collaborates_on')
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='subscribed_to')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(max_length=255, populate_from='title')

    class Meta:
        unique_together = ('slug', 'author')


    # GeoDjango-specific: a geometry field (MultiPolygonField)
    # point = models.PointField()

    # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title

    def __str__(self):
        return self.title + " by " + self.author.username

class PlaceAnnotation(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    place = models.ForeignKey(Place, related_name='annotations', on_delete=models.CASCADE)
    list = models.ForeignKey(Placelist, blank=True, null=True, related_name='place_annotations', on_delete=models.SET_NULL)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='annotations', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)


    # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        if self.list:
            tx = self.place.name + " by " + self.author.name + " for " + self.list.title
        else:
            tx = self.place.name + " by " + self.author.name
        return tx

    def __str__(self):
        if self.list:
            tx = self.place.name + " by " + self.author.name + " for " + self.list.title
        else:
            tx = self.place.name + " by " + self.author.name
        return tx

class ListUpdate(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    UPDATE_CHOICES = (
        ('add', 'Add Places'),
        ('remove', 'Remove Places')
    )
    list = models.ForeignKey(Placelist, related_name='updates', on_delete=models.CASCADE)
    # places = models.ManyToManyField(Place, related_name='list_updates')
    update_type = models.CharField(max_length=10, choices=UPDATE_CHOICES)
    update_by = models.ForeignKey(User, related_name='updates', on_delete=models.SET_DEFAULT, default=0)
    update_on = models.DateField(auto_now_add=True)


    # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return self.list.title + " by " + self.update_by.name

    def __str__(self):
        return self.list.title + " by " + self.update_by.name