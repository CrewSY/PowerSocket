"""Configuration of main URLs for PowerSocket project."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
]