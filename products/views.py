"""Views for userauth app of PowerSocket project."""

from django.db.models import Q
from django.shortcuts import render

from .models import Product
from orders.models import ProductInOrder, Order
from .utils import paginate, get_brands


def products_list(request):
    """Render home page with products list."""
    brands = get_brands(request)
    products = Product.objects.all().order_by('-publish_date')

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

    return render(request, 'main/products_list.html', context)


def update_content(request, pk):
    """Update content according received pk."""
    if pk == 'skip':
        products = Product.objects.all()
    elif pk:
        products = Product.objects.filter(brand=pk)
    else:
        products = Product.objects.all()

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
                               {'product_in_basket': set_of_id},
                               var_name='products')
        except Order.DoesNotExist:
            context = paginate(products, 9,
                               request,
                               {},
                               var_name='products')
    else:
        context = paginate(products, 9,
                           request,
                           {},
                           var_name='products')

    return render(request, 'product_content.html', context)


def search_products(request, search_by):
    """Update content according received data from search."""
    if search_by:
        q = Q()
        for tag in search_by.split():
            q |= Q(brand__brand_name__iexact=tag) | Q(model__iexact=tag)
        products = Product.objects.filter(q)
    else:
        products = Product.objects.all()

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
                               {'product_in_basket': set_of_id},
                               var_name='products')
        except Order.DoesNotExist:
            context = paginate(products, 9,
                               request,
                               {'search_by': search_by},
                               var_name='products')
    else:
        context = paginate(products, 9,
                           request,
                           {'search_by': search_by},
                           var_name='products')

    return render(request, 'main/product_content.html', context)


def new_products(request):
    """Render page with list of new products ."""
    products = Product.objects.all().order_by('-publish_date')[:10]
    brands = get_brands(request)
    return render(request, 'main/products_list.html', {'brands': brands, 'products': products})


def product_details(request, pk):
    """Render page with product details."""
    product = Product.objects.get(id=pk)
    return render(request, 'main/product_details.html', {'product': product})
