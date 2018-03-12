"""Product models for PowerSocket project."""

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    """Model that represents products."""

    class Meta:
        """Meta data of product."""

        verbose_name = _(u'Product')
        verbose_name_plural = _(u'Products')

    photo = models.ImageField(verbose_name=_(u'Photo'),
                              blank=True,
                              null=True)
    brand = models.ForeignKey('ProductBrand',
                              verbose_name=_(u'Brand'),
                              blank=False,
                              null=True,
                              on_delete=models.PROTECT)
    category = models.ForeignKey('ProductCategory',
                                 verbose_name=_(u'Category'),
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
    is_new = models.BooleanField(verbose_name=_(u'Is new'),
                                 default=False)
    discount = models.IntegerField(verbose_name=_(u'Discount'),
                                   default=0)
    rating = models.IntegerField(verbose_name=_(u'Rating'),
                                 default=0)
    count_votes = models.IntegerField(verbose_name=_(u'Count of votes'),
                                      default=0)
    is_free_delivery = models.BooleanField(verbose_name=_(u'Is free delivery'),
                                           default=True)

    def __str__(self):
        """Render the product instance as a string."""
        return u'%s %s' % (self.brand, self.model)


class ProductBrand(models.Model):
    """Model that represents brand of product."""

    class Meta:
        """Meta data of product."""

        verbose_name = _(u'Product Brand')
        verbose_name_plural = _(u'Product Brands')

    brand_name = models.CharField(verbose_name=_(u'Brand'),
                                  max_length=64)

    def __str__(self):
        """Render the brand instance as a string."""
        return self.brand_name


class ProductCategory(models.Model):
    """Model that represents category of product."""

    class Meta:
        """Meta data of category."""

        verbose_name = _(u'Product Category')
        verbose_name_plural = _(u'Product Category')

    category_name = models.CharField(verbose_name=_(u'Category'),
                                     max_length=64)

    def __str__(self):
        """Render the category instance as a string."""
        return self.category_name
