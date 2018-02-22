"""Management of admin panel."""

from django.contrib import admin  
from .models import Smartphone

admin.site.register(Smartphone)