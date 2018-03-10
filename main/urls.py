"""Configuration of main URLs for PowerSocket project."""

from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^about_us/$', TemplateView.as_view(template_name='main/about_us.html')),
]
