"""Management of admin panel."""

from django.contrib import admin
from .models import Smartphone, SmartphoneBrand


class SmartphoneAdmin(admin.ModelAdmin):
    """Class that represents smartphones at admin page."""

    list_display = ('__str__', 'price', 'publish_date', 'in_stock', )
    list_filter = ('brand', 'in_stock', )
    search_fields = ['model', 'brand__brand_name', ]

    class Meta:
        """Meta data of SmartphoneAdmin."""

        model = Smartphone


admin.site.register(Smartphone, SmartphoneAdmin)


class SmartphoneBrandAdmin(admin.ModelAdmin):
    """Class that represents smartphones brands at admin page."""

    list_display = ('brand_name', )
    list_filter = ('brand_name', )
    search_fields = ['brand_name', ]

    class Meta:
        """Meta data of SmartphoneBrandsAdmin."""

        model = SmartphoneBrand


admin.site.register(SmartphoneBrand, SmartphoneBrandAdmin)
