# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count

import json

from .models import Placelist, Place, PlaceType, ListType
from .serializers import PlacelistSerializer, PlacelistReadSerializer
from cities.models import City, Neighborhood
from django.contrib.auth.models import User
from pprint import pprint
from datetime import datetime

# Create your views here.

class ListOfLists(APIView):

    def get(self, request):
        lists = Placelist.objects.all()\
            .annotate(num_followers=Count('subscribers'))\
            .annotate(num_places=Count('places'))\
            .order_by('-num_followers', '-num_places')
        sz = PlacelistSerializer(lists, many=True)

        return Response(sz.data)

    def post(self, request):
        plob = request.data
        typ = ListType.objects.filter(name=plob['type'])
        if len(typ) > 0:
            tobj = typ[0]
        else:
            tobj = ListType.objects.create(name=plob['type'])
            tobj.save()
        print(plob['author'])
        pl = Placelist.objects.create(
            title = plob['title'],
            type = tobj,
            author = User.objects.get(username=plob['author'])
        )
        if 'description' in plob:
            pl.description = plob['description']
        if 'city' in plob:
            pl.city = City.objects.get(id=plob['city']['id'])
        if 'neighborhood' in plob:
            pl.neighborhood = Neighborhood.objects.get(id=plob['neighborhood']['id'])
        pl.save()
        sz = PlacelistReadSerializer(pl)

        return Response(sz.data)

class UserLists(APIView):

    def get(self, request, username):
        lists = Placelist.objects.filter(author__username=username)\
            .annotate(num_followers=Count('subscribers'))\
            .annotate(num_places=Count('places'))\
            .order_by('-num_followers', '-num_places')
        sz = PlacelistSerializer(lists, many=True)

        return Response(sz.data)

class ListDetail(APIView):

    def get(self, request, username, slug):
        lists = Placelist.objects.get(author__username=username, slug=slug)
        sz = PlacelistReadSerializer(lists)

        return Response(sz.data)

class CreateNewList(APIView):

    def post(self, request):
        plob = request.data
        typ = ListType.objects.filter(name=plob['type'])
        if len(typ) > 0:
            tobj = typ[0]
        else:
            tobj = ListType.objects.create(name=plob['type'])
            tobj.save()

        pl = Placelist.objects.create(
            title = plob['title'],
            type = tobj,
            author = User.objects.get(username=plob['author'])
        )
        if 'description' in plob:
            pl.description = plob['description']
        if 'city' in plob:
            pl.city = City.objects.get(id=plob['city']['id'])
        if 'neighborhood' in plob:
            pl.neighborhood = Neighborhood.objects.get(id=plob['neighborhood']['id'])
        pl.save()
        sz = PlacelistReadSerializer(pl)

        return Response(sz.data)

class AddPlaceToList(APIView):

    def post(self, request, username, slug):
        list = Placelist.objects.get(author__username=username, slug=slug)

        places = request.data
        pprint(places)
        for pl in places:
            ob_exists = Place.objects.filter(name=pl['name'], city__name=pl['city'], address=pl['address'])
            type = PlaceType.objects.filter(name=pl['type'])
            if len(type) > 0:
                tobj = type[0]
            else:
                tobj = PlaceType.objects.create(name=pl['type'])
                tobj.save()
            city = City.objects.get(name=pl['city'], state=pl['state'])
            neighborhood_exists = Neighborhood.objects.filter(name=pl['neighborhood'], city__name=pl['city'])
            if len(neighborhood_exists) > 0:
                nobj = neighborhood_exists[0]
            else:
                nobj = Neighborhood.objects.create(name=pl['neighborhood'], city=city)
            if len(ob_exists) == 0:
                pl_obj = Place.objects.create(
                    name = pl['name'],
                    type = tobj,
                    city = city,
                    neighborhood = nobj,
                    address = pl['address'],
                    lat = pl['latitude'],
                    lon = pl['longitude'],
                    google_id = pl['google_id']
                )
                if 'url' in pl:
                    pl_obj.url = pl['url']
                pl_obj.save()
            else:
                pl_obj = ob_exists[0]

            list.places.add(pl_obj)
            list.updated_on = datetime.now()
            list.save()

        list = Placelist.objects.get(author__username=username, slug=slug)

        sz = PlacelistReadSerializer(list)

        return Response(sz.data)