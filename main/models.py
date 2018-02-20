"""Models for PowerSocket project."""

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class Smartphone(models.Model):
    """Model that represents goods."""

    photo = models.ImageField(upload_to='static/img/',
                              verbose_name=_(u'Photo'),
                              blank=True,
                              null=True)
    title = models.CharField(verbose_name=_(u'Title'),
                             max_length=200)
    description = models.TextField(verbose_name=_(u'Text'))
    price = models.FloatField(verbose_name=_(u'Price'))
    publish_date = models.DateTimeField(verbose_name=_(u'Created date'),
                                        default=timezone.now)

    def __str__(self):
        """Render the smartphone instance as a string."""
        return self.title
