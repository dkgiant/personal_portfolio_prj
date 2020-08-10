"""
wsgi config for personal_portfolio project.

it exposes the wsgi callable as a module-level variable named ``application``.

for more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('django_settings_module', 'personal_portfolio.settings')

application = get_wsgi_application()
