"""Models for PowerSocket project."""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class UserProfile(models.Model):
    """Extra user data."""

    class Meta(object):
        """Meta data for user profile."""

        verbose_name = _(u'User Profile')

    user = models.OneToOneField(User)
    full_name = models.CharField(verbose_name=_(u'Full name'),
                                 max_length=64,
                                 blank=True)

    phone_number = models.CharField(verbose_name=_(u'Phone number'),
                                    max_length=48,
                                    blank=True)
    address = models.CharField(verbose_name=_(u'Address'),
                               max_length=128,
                               blank=True)

    def __str__(self):
        """Render the user instance as a string."""
        if self.full_name:
            return self.full_name
        else:
            return self.user.username
