"""Models for PowerSocket project."""

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from main.models import Product


class Order(models.Model):
    """Model that represents orders."""

    class Meta:
        """Meta data of order."""

        verbose_name = _(u'Order')
        verbose_name_plural = _(u'Orders')

    STATUS_CHOICES = (
        ('New', 'New'),
        ('In process', 'In process'),
        ('Completed', 'Completed'),
        ('Closed', 'Closed',)
    )
    owner = models.OneToOneField(User)
    status = models.CharField(verbose_name=_(u'Status'),
                              max_length=12,
                              choices=STATUS_CHOICES,
                              default='New')
    total_price = models.DecimalField(verbose_name=_(u'Total price'),
                                      max_digits=8,
                                      decimal_places=2,
                                      default=0)
    customer_name = models.CharField(verbose_name=_(u'Customer name'),
                                     blank=True,
                                     max_length=64)
    customer_email = models.EmailField(verbose_name=_(u'Customer email'),
                                       blank=True,
                                       null=True)
    customer_phone = models.CharField(verbose_name=_(u'Customer phone'),
                                      max_length=48,
                                      blank=True)
    customer_address = models.CharField(verbose_name=_(u'Customer address'),
                                        max_length=128,
                                        blank=True)
    comments = models.TextField(verbose_name=_(u'Comments'), blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        """Render the order instance as a string."""
        return '%s - %s' % (self.id, self.status)


class ProductInOrder(models.Model):
    """Model that represents product in order."""

    class Meta:
        """Meta data of product in order."""

        verbose_name = _(u'Product in order')
        verbose_name_plural = _('Products in orders')

    order = models.ForeignKey(Order,
                              verbose_name=_(u'Order'),
                              blank=True,
                              null=True)
    product = models.ForeignKey(Product,
                                verbose_name=_(u'Product'),
                                blank=True,
                                null=True)
    count = models.IntegerField(verbose_name=_(u'Count'),
                                default=1)
    price_per_item = models.DecimalField(verbose_name=_(u'Price per item'),
                                         max_digits=6,
                                         decimal_places=2,
                                         default=0)
    total_price = models.DecimalField(verbose_name=_(u'Total price'),
                                      max_digits=8,
                                      decimal_places=2,
                                      default=0)

    def __str__(self):
        """Render the product in order instance as a string."""
        return '%s %s' % (self.product.brand.brand_name, self.product.model)

    def save(self, *args, **kwargs):
        """Save product in order in data base."""
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.count * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    """Post save of product in order."""
    order = instance.order
    all_product_in_order = ProductInOrder.objects.filter(order=order,
                                                         product__in_stock=True)

    order_total_price = 0
    for item in all_product_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)
