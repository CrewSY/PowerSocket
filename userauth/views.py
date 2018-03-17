"""Views for userauth app of PowerSocket project."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import UserProfile


@login_required
def profile(request):
    """Render profile page."""
    user = request.user
    return render(request, 'registration/profile.html', {'user': user})


def profile_update(request):
    """Render profile page."""
    user = request.user
    data = request.POST
    userprofile, created = UserProfile.objects.get_or_create(user=user)

    first_name = data.get('first_name')
    if first_name != 'first name':
        user.first_name = first_name

    last_name = data.get('last_name')
    if last_name != 'last name':
        user.last_name = last_name

    phone_number = data.get('phone_number')
    if phone_number != 'phone number':
        userprofile.phone_number = phone_number

    address = data.get('address')
    if address != 'address':
        userprofile.address = address

    user.save()
    userprofile.save()

    return HttpResponse()
