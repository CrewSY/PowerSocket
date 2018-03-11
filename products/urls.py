"""Configuration of products URLs for PowerSocket project."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='home'),
    url(r'^new_products/$', views.ProductList.as_view(), name='new_products'),
    url(r'^rated_products/$', views.ProductList.as_view(), name='rated_products'),

    url(r'^product_details/(?P<pk>[0-9]+)/$', views.product_details, name='product_details'),
    url(r'^update_rating/$', views.update_rating, name='update_rating'),

    url(r'^search_products/$', views.search_products, name='search_products'),
    url(r'^update_content/$', views.UpdateContent.as_view(), name='update_content'),
]
