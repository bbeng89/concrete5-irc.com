#settings/local.py
from os import environ
from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['concrete5-irc.com', 'www.concrete5-irc.com']

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = environ['SMTP_USER']
EMAIL_HOST_PASSWORD = environ['SMTP_PASS']
DEFAULT_FROM_EMAIL = 'bot@concrete5-irc.com'
SERVER_EMAIL = 'bot@concrete5-irc.com'

STATIC_ROOT = '/home/bbeng89/webapps/concrete5_irc_static'

STATIC_URL = 'http://concrete5-irc.com/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 	# Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': environ['LIVE_DB_NAME'],
        'USER': environ['LIVE_DB_USER'],
        'PASSWORD': environ['LIVE_DB_PASS'],
        'HOST': '',                      		# Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      		# Set to empty string for default.
    }
}