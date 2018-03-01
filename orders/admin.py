"""Management of admin panel."""

from django.contrib import admin
from .models import Order, SmartphoneInOrder


class SmartphoneInOrderInline(admin.TabularInline):
    """Additional field to Order on admin page."""

    model = SmartphoneInOrder
    extra = 0


class OrderAdmin (admin.ModelAdmin):
    """Config order on admin page."""

    list_display = ('id', 'status', 'total_price', )
    list_filter = ('status', )
    inlines = [SmartphoneInOrderInline]

    class Meta:
        """Meta data of OrderAdmin."""

        model = Order


admin.site.register(Order, OrderAdmin)


class SmartphoneInOrderAdmin(admin.ModelAdmin):
    """Config smartphone in order on admin page."""

    list_display = [field.name for field in SmartphoneInOrder._meta.fields]

    class Meta:
        """Meta data of OrderAdmin."""

        model = SmartphoneInOrder


admin.site.register(SmartphoneInOrder, SmartphoneInOrderAdmin)
