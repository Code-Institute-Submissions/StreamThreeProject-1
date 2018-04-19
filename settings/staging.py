import dj_database_url

from base import *

DEBUG = False

DATABASES = {
	#'default': {
	#	'ENGINE': 'django.db.backends.sqlite3',
	#	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	#}
    'default': { dj_database_url.config('JAWSDB_URL')}
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