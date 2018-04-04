# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import PlaceType, ListType, Place, Placelist

# Register your models here.

admin.site.register(PlaceType)
admin.site.register(ListType)
admin.site.register(Place)
admin.site.register(Placelist)
