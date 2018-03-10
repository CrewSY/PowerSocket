"""Views for userauth app of PowerSocket project."""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """Render profile page."""
    user = request.user
    return render(request, 'profile.html', {'user': user})
