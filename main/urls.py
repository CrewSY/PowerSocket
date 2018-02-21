"""Configuration of main URLs for PowerSocket project."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.smartphones_list, name='home'),
    url(r'^search_smartphones/$', views.search_smartphones, name='search_smartphones'),
]
