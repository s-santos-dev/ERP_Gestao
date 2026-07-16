'''configurações só para DESENVOLVIMENTO'''

# config/settings/development.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# Email console backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug Toolbar
try:
    import debug_toolbar  # noqa: F401
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
except ImportError:
    pass

# Banco SQLite para desenvolvimento
DATABASES['default']['NAME'] = BASE_DIR / 'db_dev.sqlite3'