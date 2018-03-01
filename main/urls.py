"""Configuration of main URLs for PowerSocket project."""

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.products_list, name='home'),
    url(r'^search_products/$', views.search_products, name='search_products'),
    url(r'^about_us/$', TemplateView.as_view(template_name='main/about_us.html')),
    url(r'^basket/$', views.basket, name='basket'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^new_products/$', views.new_products, name='new_products'),
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
]
