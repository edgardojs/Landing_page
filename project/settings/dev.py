"""
Development settings.
"""

from .base import *

DEBUG = True

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-0x-&opr2i=e5=hz%&qksws9*xap&h&hv&o9cmqxzu8*-'
)

ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
    if h.strip()
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
