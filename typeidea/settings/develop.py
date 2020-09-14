# __author__ = 'MA Yu'
# __time__ = '9/14/2020 3:48 PM'

from .base import *  # NOQA，这个注释的意思是告诉PEP8规范检查工具，此处不需要检测

DEBUG = True
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
