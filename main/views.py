"""Views for main app of PowerSocket project."""

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from .models import Smartphone, SmartphoneBrand
from orders.models import SmartphoneInBasket
from .utils import paginate, get_current_brand

from orders.models import SmartphoneInOrder, Order


def smartphones_list(request):
    """Render page with smartphones list."""
    current_brand = get_current_brand(request)
    if current_brand:
        smartphones = Smartphone.objects.filter(brand=current_brand)
    else:
        smartphones = Smartphone.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'price', 'publish_date'):
        smartphones = smartphones.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            smartphones = smartphones.reverse()
    else:
        request.GET.order_by = 'publish_date'
        smartphones = smartphones.order_by('publish_date')

    brands = SmartphoneBrand.objects.all().order_by('brand_name')
    context = paginate(smartphones, 6, request, {'brands': brands}, var_name='smartphones')
    return render(request, 'main/smartphones_list.html', context)


def search_smartphones(request):
    """Render page with specific smartphones list."""
    search_by = request.GET.get('q')
    if search_by:
        q = Q()
        for tag in request.GET.get('q').split():
            q |= Q(brand__brand_name__iexact=tag) | Q(model__iexact=tag)
        smartphones = Smartphone.objects.filter(q)
    else:
        smartphones = Smartphone.objects.all()
    context = paginate(smartphones, 10, request, {'search_by': search_by}, var_name='smartphones')
    return render(request, 'main/search_results.html', context)


def basket(request):
    """Render page with list of smartphones in basket."""
    owner = request.user

    try:
        order = Order.objects.get(owner=owner)
    except Exception:
        order = None

    if order:
        smartphones = SmartphoneInOrder.objects.filter(order=order)
        return render(request, 'main/basket.html', {'order': order, 'smartphones': smartphones})
    else:
        return render(request, 'main/basket.html', {})


def profile(request):
    """Render profile page."""
    user = request.user
    return render(request, 'main/profile.html', {'user': user})


def new_products(request):
    """Render page with list of new smartphones ."""
    smartphones = Smartphone.objects.all().order_by('-publish_date')[:10]
    brands = SmartphoneBrand.objects.all().order_by('brand_name')
    return render(request, 'main/smartphones_list.html', {'brands': brands, 'smartphones': smartphones})


def basket_adding(request):
    """Add new smartphone to basket."""
    data = request.POST
    smartphone_id = data.get('smartphone_id')
    SmartphoneInBasket.objects.create(smartphone_id=smartphone_id)

    return HttpResponse()
