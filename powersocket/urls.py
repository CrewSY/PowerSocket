"""PowerSocket URL Configuration."""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views

urlpatterns = [
    url(r'', include('main.urls')),
    url(r'', include('products.urls')),
    url(r'', include('orders.urls')),
    url(r'', include('userauth.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/', include('registration.backends.simple.urls', namespace='users')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
