import os
from .common import *
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




DEBUG = True
for config in TEMPLATES:
    config['OPTIONS']['debug'] = DEBUG

    # Testing
INSTALLED_APPS = INSTALLED_APPS

    # Mail
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)


# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

RQ_QUEUES = {
    'default': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379'),
        'DB': 0,
        'DEFAULT_TIMEOUT': 500,
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
