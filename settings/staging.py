import dj_database_url

from base import *

DEBUG = False

DATABASES = {
	'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

SITE_URL = 'https://boiling-spire-29247.herokuapp.com/'
ALLOWED_HOSTS.append('boiling-spire-29247.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}