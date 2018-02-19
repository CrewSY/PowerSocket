"""WSGI config for PowerSocket project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'powersocket.settings')

application = get_wsgi_application()
