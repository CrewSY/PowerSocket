"""Views for userauth app of PowerSocket project."""

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from django.core.exceptions import ObjectDoesNotExist


from .models import Product
from orders.models import Order, ProductInOrder
from .utils import get_data


class ProductList(ListView):
    """Render list of products according path."""

    model = Product
    template_name = 'products_list.html'

    def get_queryset(self):
        """Create queryset acording request.path."""
        products = super(ProductList, self).get_queryset()

        if '/new_products/' in self.request.path:
            products = products.order_by('-is_new')
        elif '/rated_products/' in self.request.path:
            products = products.order_by('-rating')

        return products

    def get_context_data(self):
        """Create context data."""
        context = get_data(self.request)
        context['products'] = self.get_queryset()

        return context


class UpdateContent(ListView):
    """Update content according filter products."""

    model = Product
    template_name = 'product_content.html'

    def get(self, request):
        """Render product content with filtered queryset."""
        context = self.get_context_data()
        context['products'] = self.get_queryset()

        return render(request, self.template_name, context)

    def get_queryset(self):
        """Create queryset according request."""
        data = self.request.GET
        brand_id = data.get('brand_id')
        if brand_id:
            products = Product.objects.filter(brand=brand_id)
        else:
            products = super(UpdateContent, self).get_queryset()

        return products

    def get_context_data(self):
        """Create context data."""
        context = get_data(self.request)
        context['products'] = self.get_queryset()

        return context


def search_products(request):
    """Update content according received data from input of search."""
    search_by = request.GET.get('search_by')
    if search_by:
        q = Q()
        for tag in search_by.split(' '):
            q |= Q(brand__brand_name__iexact=tag) | Q(model__iexact=tag)
        products = Product.objects.filter(q)
    else:
        products = Product.objects.all()

    context = get_data(request)
    context['products'] = products

    return render(request, 'product_content.html', context)


def product_details(request, pk):
    """Render page with details of choosen product."""
    product = Product.objects.get(id=pk)
    try:
        vote = int(product.rating/product.count_votes)
    except ZeroDivisionError:
        vote = 0

    user = request.user
    if user.is_authenticated():
        try:
            order = Order.objects.get(owner=user)
            ProductInOrder.objects.get(order=order, product__id=pk)
            context = {'product': product, 'vote': vote, 'in_basket': True}
        except ObjectDoesNotExist:
            context = {'product': product, 'vote': vote}
    else:
        context = {'product': product, 'vote': vote}

    return render(request, 'product_details.html', context)
