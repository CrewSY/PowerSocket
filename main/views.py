"""Views for main app of PowerSocket project."""

from django.db.models import Q
from django.shortcuts import render

from .models import Smartphone, SmartphoneBrand
from .utils import paginate, get_current_brand


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
    return render(request, 'main/basket.html', {})
