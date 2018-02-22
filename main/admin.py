"""Management of admin panel."""

from django.contrib import admin
from .models import Smartphone, SmartphonesBrands

admin.site.register(Smartphone)
admin.site.register(SmartphonesBrands)
