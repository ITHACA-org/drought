"""
WSGI config for drought project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
sys.path.insert(0, '/opt/apps/drought/lib/python2.7/site-packages')
sys.path.insert(0, '/opt/apps/drought/drought')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drought.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
