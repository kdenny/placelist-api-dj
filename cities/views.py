# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count

import json
from .models import City, Neighborhood
from .serializers import CitySerializer, NeighborhoodSerializer
from lists.models import Place, Placelist
from lists.serializers import PlacelistSerializer, PlaceSerializer

# Create your views here.

class ListOfCities(APIView):

    def get(self, request):
        ct = City.objects.all().annotate(num_lists=Count('lists')).order_by('-num_lists')
        sz = CitySerializer(ct, many=True)

        return Response(sz.data)

class CityDetail(APIView):

    def get(self, request, slug):
        ct = City.objects.get(slug=slug)
        sz = CitySerializer(ct)

        return Response(sz.data)

class CityPlaces(APIView):

    def get(self, request, slug):
        ct = Place.objects.filter(city__slug=slug)

        nearby_cities = City.objects.filter(parent_city__slug=slug)
        for nc in nearby_cities:
            ncp = nearby_cities.places
            og = ncp | ct
            ct = og

        sz = PlaceSerializer(ct, many=True)

        return Response(sz.data)

class PlaceDetail(APIView):

    def get(self, request, citySlug, slug):
        ct = Place.objects.get(city__slug=citySlug, slug=slug)
        sz = PlaceSerializer(ct)

        return Response(sz.data)

class CityLists(APIView):

    def get(self, request, slug):
        ct = Placelist.objects.filter(city__slug=slug)
        sz = PlacelistSerializer(ct, many=True)

        return Response(sz.data)

class CityNeighborhoods(APIView):

    def get(self, request, slug):
        ct = Neighborhood.objects.filter(city__slug=slug)
        sz = NeighborhoodSerializer(ct, many=True)

        return Response(sz.data)