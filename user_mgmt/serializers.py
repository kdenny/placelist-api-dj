from rest_framework import serializers

from .models import UserProfile, User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

        fields = ('user', 'type', 'instagram', 'soundcloud')

class JustUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ('username', 'id')
        depth = 1