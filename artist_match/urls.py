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

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_artist/$', views.CreateArtist.as_view()),
    url(r'^load_artists/$', views.ArtistListView.as_view()),
    # url(r'^swipe/$', views.Swipe.as_view()),
    # url(r'^view_matches/$', views.ApartmentsListView.as_view()),
    # url(r'^match/(?P<match_id>[0-9]+)/$', views.PackagesListView.as_view()),
    # url(r'^messages/(?P<message_id>[0-9]+)/$', views.PackagesListView.as_view()),
]
