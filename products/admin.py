"""Management of admin panel."""

from django.contrib import admin
from .models import Product, ProductBrand, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    """Class that represents products at admin page."""

    list_display = ('__str__', 'price', 'publish_date', 'in_stock', )
    list_filter = ('brand', 'in_stock', 'is_new', )
    search_fields = ['model', 'brand__brand_name', ]

    class Meta:
        """Meta data of ProductAdmin."""

        model = Product


admin.site.register(Product, ProductAdmin)


class ProductBrandAdmin(admin.ModelAdmin):
    """Class that represents products brands at admin page."""

    list_display = ('brand_name', )
    list_filter = ('brand_name', )
    search_fields = ['brand_name', ]

    class Meta:
        """Meta data of ProductBrandsAdmin."""

        model = ProductBrand


admin.site.register(ProductBrand, ProductBrandAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    """Class that represents products brands at admin page."""

    list_display = ('category_name', )
    list_filter = ('category_name', )
    search_fields = ['category_name', ]

    class Meta:
        """Meta data of ProductCategoryAdmin."""

        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)
