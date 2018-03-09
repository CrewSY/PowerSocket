"""Views for userauth app of PowerSocket project."""

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView


from .models import Product, ProductBrand
from orders.models import ProductInOrder, Order
from .utils import paginate


class ProductListView(ListView):
    """Render list of products according path."""

    model = Product
    template_name = 'main/products_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        """Create queryset acording request.path."""
        products = super(ProductListView, self).get_queryset()

        if '/new_products/' in self.request.path:
            products = products.order_by('-is_new')
        elif '/rated_products/' in self.request.path:
            products = products.order_by('-rating')

        return products

    def get_context_data(self, **kwargs):
        """Create context data."""
        data = super().get_context_data(**kwargs)
        data['brands'] = ProductBrand.objects.all().order_by('brand_name')
        return data


class UpdateContentView(ListView):
    """Update content according filter products."""

    model = Product
    template_name = 'main/product_content.html'

    def get(self, request):
        """Render product content with filtered queryset."""
        products = self.get_queryset()

        return render(request, self.template_name, {'products': products})

    def get_queryset(self):
        """Create queryset according request."""
        data = self.request.GET
        brand_id = data.get('brand_id')
        if brand_id:
            products = Product.objects.filter(brand=brand_id)
        else:
            products = super(UpdateContentView, self).get_queryset()

        return products


def search_products(request, search_by):
    """Update content according received data from search."""
    if search_by:
        q = Q()
        for tag in search_by.split('_'):
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


def product_details(request, pk):
    """Render page with product details."""
    product = Product.objects.get(id=pk)
    try:
        vote = int(product.rating/product.count_votes)
    except ZeroDivisionError:
        vote = 0

    return render(request,
                  'main/product_details.html',
                  {'product': product,
                   'vote': vote}
                  )
