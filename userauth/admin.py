"""Management of admin panel."""

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    """Additional fields to Order on admin page."""

    model = UserProfile


class UserAdmin(auth_admin.UserAdmin):
    """Class that represents users at admin page."""

    list_display = ('__str__', 'email', )
    search_fields = ['__str__', 'email', ]
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
