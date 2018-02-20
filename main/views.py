"""Views for main app of PowerSocket project."""

from django.shortcuts import render
from django.utils import timezone

from .models import Smartphone


def smartphones_list(request):
    """Render page with goods list."""
    smartphones = Smartphone.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'main/smartphones_list.html', {'smartphones': smartphones})
