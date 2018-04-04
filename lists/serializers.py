from rest_framework import serializers

from .models import Placelist, Place

class PlacelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placelist
        depth = 1

        fields = ('title', 'type', 'places', 'description', 'city', 'neighborhood', 'author', 'collaborators', 'subscribers', 'created_on', 'updated_on', 'slug', 'place_annotations', )

class PlacelistReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placelist
        depth = 2

        fields = ('title', 'type', 'places', 'description', 'city', 'neighborhood', 'author', 'collaborators', 'subscribers', 'created_on', 'updated_on', 'slug', 'place_annotations', )

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        depth = 1

        fields = ('name', 'type', 'city', 'neighborhood', 'address', 'url', 'added_on', 'slug', 'zip_code', 'lat', 'lon', 'slug', 'annotations', 'included_in', )