#settings/local.py
from os import environ
from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = environ['SMTP_USER']
EMAIL_HOST_PASSWORD = environ['SMTP_PASS']
DEFAULT_FROM_EMAIL = 'bot@concrete5-irc.com'
SERVER_EMAIL = 'bot@concrete5-irc.com'

STATIC_ROOT = ''

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': environ['LOCAL_DB_NAME'],                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': environ['LOCAL_DB_USER'],
        'PASSWORD': environ['LOCAL_DB_PASS'],
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

#add Django Debug Toolbar settings
INSTALLED_APPS += ('debug_toolbar',)
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'EXTRA_SIGNALS': [],
    'HIDE_DJANGO_SQL': False,
    'TAG': 'div',
    'ENABLE_STACKTRACES' : True,
}