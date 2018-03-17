"""Models for PowerSocket project."""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product


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
    voted_posts = models.ManyToManyField(Product,
                                         verbose_name=_(u'Liked posts'))

    def __str__(self):
        """Render the user instance as a string."""
        if self.user.first_name and self.user.last_name:
            return '%s %s' % (self.user.first_name, self.user.last_name)
        else:
            return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create user profile after register."""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save user profile."""
    instance.userprofile.save()
