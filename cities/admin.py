# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import City, Neighborhood, State, Country

# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(State)