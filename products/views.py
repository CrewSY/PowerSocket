"""Views for userauth app of PowerSocket project."""

from django.db.models import Q
from django.shortcuts import render

from .models import Product
from .utils import paginate, get_current_brand, get_brands


def products_list(request):
    """Render page with products list."""
    current_brand = get_current_brand(request)
    if current_brand:
        products = Product.objects.filter(brand=current_brand)
    else:
        products = Product.objects.all()

    brands = get_brands(request)
    context = paginate(products, 6, request, {'brands': brands}, var_name='products')
    return render(request, 'main/products_list.html', context)


def search_products(request):
    """Render page with specific products list."""
    search_by = request.GET.get('q')
    if search_by:
        q = Q()
        for tag in request.GET.get('q').split():
            q |= Q(brand__brand_name__iexact=tag) | Q(model__iexact=tag)
        products = Product.objects.filter(q)
    else:
        products = Product.objects.all()
    context = paginate(products, 10, request, {'search_by': search_by}, var_name='products')
    return render(request, 'main/search_results.html', context)


def new_products(request):
    """Render page with list of new products ."""
    products = Product.objects.all().order_by('-publish_date')[:10]
    brands = get_brands(request)
    return render(request, 'main/products_list.html', {'brands': brands, 'products': products})


def product_details(request, pk):
    """Render page with product details."""
    product = Product.objects.get(id=pk)
    return render(request, 'main/product_details.html', {'product': product})
