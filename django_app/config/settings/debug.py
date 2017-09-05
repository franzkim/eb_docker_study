# debug.py
from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.debug.application'

# DEBUG MODE
DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

print('===== DEBUG', DEBUG)
print('===== ALLOWED_HOSTS', ALLOWED_HOSTS)
