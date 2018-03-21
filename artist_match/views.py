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


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse

from artist_match.models import ArtistProfile, Like, Message
from artist_match.serializers import ArtistCreateSerializer, ArtistReadSerializer

class CreateArtist(APIView):

    def post(self, request):
        print(request.data)

        serializer = ArtistCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("serialized!")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #################### END POST RELATED METHODS ####################

class ArtistListView(APIView):
    def get(self, request):
        artists = ArtistProfile.objects.all()
        artists_ser = ArtistReadSerializer(artists, many=True)

        return Response(artists_ser.data)
