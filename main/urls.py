"""Configuration of main URLs for PowerSocket project."""

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.smartphones_list, name='home'),
    url(r'^search_smartphones/$', views.search_smartphones, name='search_smartphones'),
    url(r'^about_us/$', TemplateView.as_view(template_name='main/about_us.html')),
    url(r'^basket/$', views.basket, name='basket'),
]
