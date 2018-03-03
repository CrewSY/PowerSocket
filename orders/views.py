"""Views for orders app of PowerSocket project."""

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from orders.models import ProductInOrder, Order
from products.models import Product


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
def basket_adding(request):
    """Add new product to basket."""
    data = request.POST
    user = request.user
    order, created = Order.objects.get_or_create(owner=user)
    product_id = data.get('product_id')
    ProductInOrder.objects.create(product_id=product_id, order=order)

    return HttpResponse()


def update_quantity(request):
    """Update quantity of product in order."""
    data = request.POST
    product_id = data.get('product_id')
    qty = data.get('qty')

    ProductInOrder.objects.filter(id=product_id).update(count=qty)

    return HttpResponse()


def remove_product(request):
    """Remove product from basket."""
    data = request.POST
    product_id = data.get('product_id')

    product = ProductInOrder.objects.filter(id=product_id)
    product.delete()

    return HttpResponse()


def update_rating(request):
    """Update quantity of product in order."""
    data = request.POST
    product_id = data.get('product_id')
    vote = data.get('vote')

    product = Product.objects.get(id=product_id)
    product.count_votes = product.count_votes + 1
    product.rating = product.rating + int(vote)

    product.save()

    return HttpResponse()
