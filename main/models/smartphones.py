"""Smartphone models for PowerSocket project."""

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Smartphone(models.Model):
    """Model that represents smartphones."""

    class Meta:
        """Meta data of smartphone."""

        verbose_name = _(u'Smartphone')
        verbose_name_plural = _(u'Smartphones')

    photo = models.ImageField(verbose_name=_(u'Photo'),
                              blank=True,
                              null=True)
    brand = models.ForeignKey('SmartphoneBrand',
                              verbose_name=_(u'Brand'),
                              blank=False,
                              null=True,
                              on_delete=models.PROTECT)
    model = models.CharField(verbose_name=_(u'Model'),
                             blank=True,
                             max_length=255)
    description = models.TextField(verbose_name=_(u'Description'),
                                   blank=True)
    price = models.DecimalField(verbose_name=_(u'Price'),
                                max_digits=8,
                                decimal_places=2,
                                default=0)
    publish_date = models.DateTimeField(verbose_name=_(u'Created date'),
                                        default=timezone.now)
    in_stock = models.BooleanField(verbose_name=_(u'In stock'),
                                   default=True)

    def __str__(self):
        """Render the smartphone instance as a string."""
        return u'%s %s' % (self.brand, self.model)


class SmartphoneBrand(models.Model):
    """Model that represents brand of smartphone."""

    class Meta:
        """Meta data of smartphone."""

        verbose_name = _(u'Smartphone Brand')
        verbose_name_plural = _(u'Smartphone Brands')

    brand_name = models.CharField(verbose_name=_(u'Brand'),
                                  max_length=64)

    def __str__(self):
        """Render the brand instance as a string."""
        return self.brand_name
