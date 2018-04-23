# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile, Friendship, GoogleAccount, FacebookAccount

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Friendship)
admin.site.register(GoogleAccount)
admin.site.register(FacebookAccount)