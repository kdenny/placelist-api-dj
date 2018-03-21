from rest_framework import serializers

from artist_match.models import ArtistProfile

class ArtistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistProfile

        fields = ('name', 'artist_type', 'genre', 'city', 'latitude', 'longitude', 'soundcloud_id' )

class ArtistReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistProfile

        fields = ('id', 'name', 'artist_type', 'genre', 'city', 'latitude', 'longitude', 'soundcloud_id' )