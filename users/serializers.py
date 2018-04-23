from rest_framework import serializers

from .models import UserProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        depth = 1

        fields = ('user', 'name', 'registered_on', 'last_active', 'city', 'neighborhood', )