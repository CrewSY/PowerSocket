"""Configuration of main URLs for PowerSocket project."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^basket/$', views.basket, name='basket'),
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^update_quantity/$', views.update_quantity, name='update_quantity'),
]
