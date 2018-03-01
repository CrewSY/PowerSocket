"""Management of admin panel."""

from django.contrib import admin
from .models import Order, ProductInOrder


class ProductInOrderInline(admin.TabularInline):
    """Additional field to Order on admin page."""

    model = ProductInOrder
    extra = 0


class OrderAdmin (admin.ModelAdmin):
    """Config order on admin page."""

    list_display = ('id', 'status', 'total_price', )
    list_filter = ('status', )
    inlines = [ProductInOrderInline]

    class Meta:
        """Meta data of OrderAdmin."""

        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    """Config product in order on admin page."""

    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        """Meta data of OrderAdmin."""

        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)
