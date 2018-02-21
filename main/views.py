"""Views for main app of PowerSocket project."""

from django.shortcuts import render
from django.utils import timezone

from .models import Smartphone
from .util import paginate


def smartphones_list(request):
    """Render page with goods list."""
    smartphones = Smartphone.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    order_by = request.GET.get('order_by', '')
    request.GET.order_by = 'publish_date'

    if order_by in ('title', 'price', 'publish_date'):
        smartphones = smartphones.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            smartphones = smartphones.reverse()

    context = paginate(smartphones, 6, request, {}, var_name='smartphones')
    return render(request, 'main/smartphones_list.html', context)
