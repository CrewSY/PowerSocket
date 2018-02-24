"""PowerSocket URL Configuration."""

from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    url(r'', include('main.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^admin/', admin.site.urls),
]