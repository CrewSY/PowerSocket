"""Models for PowerSocket project."""

from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from main.models import Smartphone


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
    status = models.CharField(verbose_name=_(u'Status'),
                              max_length=12,
                              choices=STATUS_CHOICES,
                              default='1')
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


class SmartphoneInOrder(models.Model):
    """Model that represents smartphone in order."""

    class Meta:
        """Meta data of smartphone in order."""

        verbose_name = _(u'Smartphone in order')
        verbose_name_plural = _('Smartphones in orders')

    order = models.ForeignKey(Order,
                              verbose_name=_(u'Order'),
                              blank=True,
                              null=True)
    smartphone = models.ForeignKey(Smartphone,
                                   verbose_name=_(u'Smartphone'),
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
        """Render the smartphone in order instance as a string."""
        return '%s %s' % (self.smartphone.brand.brand_name, self.smartphone.model)

    def save(self, *args, **kwargs):
        """Save smartphone in order in data base."""
        price_per_item = self.smartphone.price
        self.price_per_item = price_per_item
        self.total_price = self.count * price_per_item

        super(SmartphoneInOrder, self).save(*args, **kwargs)


def smartphone_in_order_post_save(sender, instance, created, **kwargs):
    """Post save of smartphone in order."""
    order = instance.order
    all_smartphone_in_order = SmartphoneInOrder.objects.filter(order=order,
                                                               smartphone__in_stock=True)

    order_total_price = 0
    for item in all_smartphone_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(smartphone_in_order_post_save, sender=SmartphoneInOrder)


class SmartphoneInBasket(models.Model):
    """Model that represents smartphone in basket."""

    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    smartphone = models.ForeignKey(Smartphone, blank=True, null=True)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        """Render the smartphone in order instance as a string."""
        return '%s %s' % (self.smartphone.brand.brand_name, self.smartphone.model)

    def save(self, *args, **kwargs):
        """Save smartphone in basket in data base."""
        price_per_item = self.smartphone.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item

        super(SmartphoneInBasket, self).save(*args, **kwargs)
