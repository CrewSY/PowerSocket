"""
Global functions for main app of PowerSocket project.

  - def paginate(objects, size, request, context, var_name) - > context

"""
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    from .models import SmartphonesBrands

    # cur_brand = get_current_brand(request)

    brands = []
    for brand in SmartphonesBrands.objects.all().order_by('brand_name'):
        brands.append({
            'id': brand.id,
            'brand_name': brand.brand_name,
            # 'selected': cur_group and cur_group.id == group.id and True or False
        })
    return brands
