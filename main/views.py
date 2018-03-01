"""Views for main app of PowerSocket project."""

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Product, ProductBrand
from orders.models import ProductInOrder, Order
from .utils import paginate, get_current_brand


def products_list(request):
    """Render page with products list."""
    current_brand = get_current_brand(request)
    if current_brand:
        products = Product.objects.filter(brand=current_brand)
    else:
        products = Product.objects.all()

    brands = ProductBrand.objects.all().order_by('brand_name')
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


@login_required
def basket(request):
    """Render page with list of products in basket."""
    owner = request.user

    try:
        order = Order.objects.get(owner=owner)
    except Exception:
        order = None

    if order:
        products = ProductInOrder.objects.filter(order=order)
        return render(request, 'main/basket.html', {'order': order, 'products': products})
    else:
        return render(request, 'main/basket.html', {})


@login_required
def profile(request):
    """Render profile page."""
    user = request.user
    return render(request, 'main/profile.html', {'user': user})


def new_products(request):
    """Render page with list of new products ."""
    products = Product.objects.all().order_by('-publish_date')[:10]
    brands = ProductBrand.objects.all().order_by('brand_name')
    return render(request, 'main/products_list.html', {'brands': brands, 'products': products})


@login_required
def basket_adding(request):
    """Add new product to basket."""
    data = request.POST
    user = request.user
    order, created = Order.objects.get_or_create(owner=user)
    product_id = data.get('product_id')
    ProductInOrder.objects.create(product_id=product_id, order=order)

    return HttpResponse()


def smartphone_details(request):
    """Render page with smartphone_details."""
    return render(request, 'main/smartphone_details.html', {})
