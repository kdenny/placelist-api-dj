from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=25)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    soundcloud = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username
