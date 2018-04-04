from rest_framework import serializers

from cities.models import City, Neighborhood

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        depth = 2

        fields = ('name', 'country', 'state', 'parent_city', 'slug', 'city_class', 'neighborhoods', 'lists', 'places', )

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        depth = 1

        fields = ('name', 'city', 'slug', 'lists', )