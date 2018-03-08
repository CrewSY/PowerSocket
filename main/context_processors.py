"""Context prosserors of main app for PowerSocket project."""

from products.utils import get_count_basket_products


def count_products_processor(request):
    """Return count of products in basket."""
    return {'count_products': get_count_basket_products(request)}
