# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from cities.models import City, Neighborhood

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_name = models.CharField(max_length=25)
    registered_on = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now_add=True)

    city = models.ForeignKey(City, blank=True, null=True, related_name='users', on_delete=models.SET_NULL)
    neighborhood = models.ForeignKey(Neighborhood, blank=True, null=True, related_name='users', on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.login_name

    def __str__(self):
        return self.login_name

class Friendship(models.Model):
    user1 = models.OneToOneField(User, related_name='following', on_delete=models.CASCADE)
    user2 = models.OneToOneField(User, related_name='followers', on_delete=models.CASCADE)
    friends_since = models.DateTimeField(auto_now_add=True)
    reciprocal = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user1.login_name + " - " + self.user2.login_name

    def __str__(self):
        return self.user1.login_name + " - " + self.user2.login_name