"""Configuration of products URLs for PowerSocket project."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.products_list, name='home'),
    url(r'^search_products/$', views.search_products, name='search_products'),
    url(r'^new_products/$', views.new_products, name='new_products'),
    url(r'^smartphone_details/$', views.smartphone_details, name='smartphone_details'),
]
