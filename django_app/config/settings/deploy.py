# deploy.py
from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# DEBUG MODE
DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

print('===== DEBUG', DEBUG)
print('===== ALLOWED_HOSTS', ALLOWED_HOSTS)
