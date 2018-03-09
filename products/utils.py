"""
Global functions for main app of PowerSocket project.

  - def get_basket_products(request, products, brands) -> context data
  - def get_count_basket_products(request) -> count products

"""

from orders.models import ProductInOrder, Order
from products.models import ProductBrand, ProductCategory


def get_data(request):
    """Return context with paginated products."""
    user = request.user
    brands = ProductBrand.objects.all().order_by('brand_name')
    categories = ProductCategory.objects.all().order_by('category_name')
    if user.is_authenticated():
        try:
            order = Order.objects.get(owner=user)
            product_in_basket = ProductInOrder.objects.filter(order=order)
            set_of_id = set()
            for pr in product_in_basket:
                set_of_id.add(pr.product.id)
            context = {'product_in_basket': set_of_id,
                       'brands': brands,
                       'categories': categories}
        except Order.DoesNotExist:
            context = {'brands': brands,
                       'categories': categories}
    else:
        context = {'brands': brands,
                   'categories': categories}

    return context


def get_count_basket_products(request):
    """Return count of products in basket."""
    user = request.user
    if user.is_authenticated():
        try:
            order = Order.objects.get(owner=user)
            products_in_basket = ProductInOrder.objects.filter(order=order)
            count_products = len(products_in_basket)
        except Order.DoesNotExist:
            count_products = 0
    else:
        count_products = 0

    return count_products
