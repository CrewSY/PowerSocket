"""
Global functions for main app of PowerSocket project.

  - def paginate(objects, size, request, context, var_name) -> context
  - def get_brand(request) -> objects:brands
  - def get_basket_products(request, products, brands) -> context
  - def get_count_basket_products(request) -> count products
"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from orders.models import ProductInOrder, Order


def paginate(objects, size, request, context, var_name='object_list'):
    """Paginate objects."""
    paginator = Paginator(objects, size)
    page = request.GET.get('page', '1')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    context[var_name] = object_list
    context['is_paginated'] = object_list.has_other_pages()
    context['page_obj'] = object_list
    context['paginator'] = paginator

    return context


def get_brands(request):
    """Return all brands."""
    from .models import ProductBrand

    brands = []
    for brand in ProductBrand.objects.all().order_by('brand_name'):
        brands.append({
            'id': brand.id,
            'brand_name': brand.brand_name,
        })
    return brands


def get_basket_products(request, products, brands):
    """Return context with paginated products."""
    user = request.user

    if user.is_authenticated():
        try:
            order = Order.objects.get(owner=user)
            product_in_basket = ProductInOrder.objects.filter(order=order)
            set_of_id = set()
            for pr in product_in_basket:
                set_of_id.add(pr.product.id)
            context = paginate(products, 9,
                               request,
                               {'product_in_basket': set_of_id,
                                'brands': brands},
                               var_name='products')
        except Order.DoesNotExist:
            context = paginate(products, 9,
                               request,
                               {'brands': brands},
                               var_name='products')
    else:
        context = paginate(products, 9,
                           request,
                           {'brands': brands},
                           var_name='products')
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
