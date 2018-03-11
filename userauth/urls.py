"""Configuration of main URLs for PowerSocket project."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/update/$', views.profile_update, name='profile_update'),
]
