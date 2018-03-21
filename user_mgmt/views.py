# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.http import HttpResponse


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserProfileSerializer, JustUserSerializer
from .models import UserProfile, User

# Create your views here.

from rest_framework.response import Response


class Username(APIView):
    def get(self, request):
        current_user = request.user.username

        uu = User.objects.get(username=current_user)

        rp = UserProfile.objects.get(user=uu.id)
        rs = UserProfileSerializer(rp)

        data = {
            'resident': rs.data
        }

        return Response(data)
