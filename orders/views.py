"""Views for orders app of PowerSocket project."""

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from orders.models import ProductInOrder, Order


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
        return render(request, 'basket.html', {'order': order, 'products': products})
    else:
        return render(request, 'basket.html', {})


@login_required
def basket_adding(request):
    """Add new product to basket."""
    data = request.POST
    user = request.user
    order, created = Order.objects.get_or_create(owner=user)
    product_id = data.get('product_id')
    print(product_id)
    ProductInOrder.objects.create(product_id=product_id, order=order)

    return HttpResponse()


def update_quantity(request):
    """Update quantity of product in order."""
    data = request.POST
    product_id = data.get('product_id')
    qty = data.get('qty')

    product = ProductInOrder.objects.get(id=product_id)
    product.count = qty
    product.save()

    return HttpResponse()


def remove_product(request):
    """Remove product from basket."""
    data = request.POST
    product_id = data.get('product_id')

    product = ProductInOrder.objects.filter(id=product_id)
    product.delete()

    return HttpResponse()
