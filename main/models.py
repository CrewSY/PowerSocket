"""Models for PowerSocket project."""

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Smartphone(models.Model):
    """Model that represents smartphones."""

    photo = models.ImageField(verbose_name=_(u'Photo'),
                              blank=True,
                              null=True)
    brand = models.ForeignKey('SmartphonesBrands',
                              verbose_name=_(u'Brand'),
                              blank=False,
                              null=True,
                              on_delete=models.PROTECT)
    model = models.CharField(verbose_name=_(u'Model'),
                             max_length=255)
    description = models.TextField(verbose_name=_(u'Description'))
    price = models.FloatField(verbose_name=_(u'Price'))
    publish_date = models.DateTimeField(verbose_name=_(u'Created date'),
                                        default=timezone.now)

    def __str__(self):
        """Render the smartphone instance as a string."""
        return u'%s %s' % (self.brand, self.model)


class SmartphonesBrands(models.Model):
    """Model that represents brands of smartphones."""

    brand_name = models.CharField(verbose_name=_(u'Brand'),
                                  max_length=64)

    def __str__(self):
        """Render the brand instance as a string."""
        return self.brand_name
