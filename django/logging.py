TODAY = date.today().strftime('%Y%m%d')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'dbfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/db-' + TODAY + '.log',
            'formatter': 'verbose',
        },
        'djangofile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/django-' + TODAY + '.log',
            'formatter': 'verbose',
        },
        'usersappfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/users-' + TODAY + '.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'djangofile', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['dbfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'djangofile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'users': {
            'handlers': ['console', 'usersappfile'],
            'level': 'DEBUG',
        },
    }
}
