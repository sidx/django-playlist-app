from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^tracks$', views.tracks_list, name='tracks_list'),
    url(r'^genres$', views.genre_list, name='genre_list'),
    url(r'^genre/(?P<id>\d+)/$', views.genre_detail, name='genre_detail'),
    url(r'^track/(?P<id>\d+)/$', views.track_detail, name='track_detail'),
]
