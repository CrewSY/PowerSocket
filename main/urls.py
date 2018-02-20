"""Configuration of main URLs for PowerSocket project."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.smartphones_list, name='home'),
]
