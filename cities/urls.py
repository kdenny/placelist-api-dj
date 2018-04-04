from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListOfCities.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', views.CityDetail.as_view()),
    url(r'^(?P<slug>[\w-]+)/lists/$', views.CityLists.as_view()),
    url(r'^(?P<slug>[\w-]+)/places/$', views.CityPlaces.as_view()),
    url(r'^(?P<citySlug>[\w-]+)/places/(?P<slug>[\w-]+)/$', views.PlaceDetail.as_view()),
    url(r'^(?P<slug>[\w-]+)/neighborhoods/$', views.CityNeighborhoods.as_view()),
    # url(r'^load_artists/$', views.ArtistListView.as_view()),
    # url(r'^swipe/$', views.Swipe.as_view()),
    # url(r'^view_matches/$', views.ApartmentsListView.as_view()),
    # url(r'^match/(?P<match_id>[0-9]+)/$', views.PackagesListView.as_view()),
    # url(r'^messages/(?P<message_id>[0-9]+)/$', views.PackagesListView.as_view()),
]