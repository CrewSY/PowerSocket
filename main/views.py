"""Views for main app of PowerSocket project."""

from django.shortcuts import render

from .models import Smartphone, SmartphonesBrands
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

    brands = SmartphonesBrands.objects.all().order_by('brand_name')
    context = paginate(smartphones, 6, request, {'brands': brands}, var_name='smartphones')
    return render(request, 'main/smartphones_list.html', context)


def search_smartphones(request):
    """Render page with specific smartphones list."""
    search_by = request.GET.get('search_by')
    smartphones = Smartphone.objects.get(title__contains=search_by)

    context = paginate(smartphones, 6, request, {}, var_name='smartphones')
    return render(request, 'main/smartphones_list.html', context)
