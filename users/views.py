# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile, FacebookAccount, GoogleAccount
from cities.models import City
from django.contrib.auth.models import User
from .serializers import ProfileSerializer
# Create your views here.

class CheckUserExists(APIView):

    def post(self, request):
        plob = request.data
        profile = None
        po = {}
        if plob['type'] == 'google':
            ga = GoogleAccount.objects.filter(google_id=plob['id'])
            pb = UserProfile.objects.filter(google_account__google_id=plob['id'])
            if len(pb) == 1:
                profile = pb[0]
        if plob['type'] == 'facebook':
            pb = UserProfile.objects.filter(facebook_account__facebook_id=plob['id'])
            if len(pb) == 1:
                profile = pb[0]
        if profile is None:
            po['profile'] = 'None'
            return Response(po)
        else:
            print(profile)
            user = profile.user
            lists = user.lists_created
            print(lists)
            ps = ProfileSerializer(profile)
            data = {
                'profile': ps.data
            }
            return Response(data)

class Register(APIView):

    def post(self, request):
        plob = request.data
        profile = None
        uo = User.objects.create(email=request.data['email'], password='password', username=request.data['username'])
        if request.data['first_name']:
            uo.first_name = request.data['first_name']
        if request.data['last_name']:
            uo.last_name = request.data['last_name']
        uo.save()
        ct = City.objects.filter(name=request.data['city'])

        up = UserProfile.objects.create(user=uo, name=request.data['display_name'])

        if request.data['type'] == 'google':
            ga = GoogleAccount.objects.create(google_id=request.data['id'], display_name=request.data['display_name'])
            ga.save()
            up.google_account = ga
            up.save()
        if request.data['type'] == 'facebook':
            fa = FacebookAccount.objects.create(facebook_id=request.data['id'], display_name=request.data['display_name'])
            fa.save()
            up.facebook_account = fa
            up.save()

        if len(ct) > 0:
            up.city = ct[0]
            up.save()

        ps = ProfileSerializer(profile)
        return Response(ps.data)