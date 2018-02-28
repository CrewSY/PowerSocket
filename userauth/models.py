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
    phone_number = models.CharField(verbose_name=_(u'Phone number'),
                                    max_length=48,
                                    blank=True)
    address = models.CharField(verbose_name=_(u'Address'),
                               max_length=128,
                               blank=True)

    def __str__(self):
        """Render the user instance as a string."""
        if self.user.first_name and self.user.last_name:
            return '%s %s' % (self.user.first_name, self.user.last_name)
        else:
            return self.user.username
