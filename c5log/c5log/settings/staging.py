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

STATIC_ROOT = '/home/bbeng89/webapps/c5log_staging_static'

STATIC_URL = 'http://staging.concrete5-irc.com/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 	# Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': environ['STAGING_DB_NAME'],
        'USER': environ['STAGING_DB_USER'],
        'PASSWORD': environ['STAGING_DB_PASS'],
        'HOST': '',                      		# Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      		# Set to empty string for default.
    }
}