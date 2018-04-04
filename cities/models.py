# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=3, primary_key=True)

    def __unicode__(self):
        return self.abbreviation

    def __str__(self):
        return self.abbreviation

class Country(models.Model):
    name = models.CharField(max_length=150, primary_key=True)
    country_code = models.CharField(max_length=3)
    CONT_CHOICES = (
        ('na', 'North America'),
        ('sa', 'South America'),
        ('eu', 'Europe'),
        ('as', 'Asia'),
        ('af', 'Africa'),
        ('au', 'Austrailia'),
    )
    continent = models.CharField(max_length=2, choices=CONT_CHOICES)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=150)
    state = models.ForeignKey(State, related_name='cities', blank=True, null=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='cities', default='United States', on_delete=models.CASCADE)
    parent_city = models.ManyToManyField("self", blank=True, null=True, related_name='sub_cities')
    slug = AutoSlugField(max_length=255, populate_from='name')
    CITY_CLASS_CHOICES = (
        ('primary', 'Primary City'),
        ('nearby', 'Nearby City'),
        ('suburb', 'Suburb')
    )
    city_class = models.CharField(max_length=20,default='primary', choices=CITY_CLASS_CHOICES)

    # city = models.ForeignKey(City)

    def __unicode__(self):
        if self.state:
            a = self.state.abbreviation
        else:
            a = self.country.name
        return self.name

    def __str__(self):
        if self.state:
            a = self.state.abbreviation
        else:
            a = self.country.name
        return self.name + ", " + a


class Neighborhood(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey(City, related_name='neighborhoods', on_delete=models.CASCADE)
    slug = AutoSlugField(max_length=255, populate_from='name')

    class Meta:
        unique_together = ('slug', 'city')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name + ", " + self.city.name