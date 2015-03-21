"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
<<<<<<< HEAD
=======
from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = \
global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
"django.core.context_processors.request",
"studentsdb.context_processors.students_proc",
)
PORTAL_URL = 'http://localhost:8000'
>>>>>>> a83d2d578620aae3f409aba2a4e17a0ec48f0334

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
SECRET_KEY = 'guc3&6pa^$-1h^6%z!62#al%1)9cft54e4*tt&iixatw*$92cl'
=======
SECRET_KEY = 'u1_97z^c!5kpxtivxqru5k7j29553zq6@x^x%7t@yyqxi&m4fl'
>>>>>>> a83d2d578620aae3f409aba2a4e17a0ec48f0334

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
=======
    'students',
>>>>>>> a83d2d578620aae3f409aba2a4e17a0ec48f0334
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
<<<<<<< HEAD
        'NAME': os.path.join(BASE_DIR, '..',  'db.sqlite3'),
    }
}

=======
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
>>>>>>> a83d2d578620aae3f409aba2a4e17a0ec48f0334
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
<<<<<<< HEAD
=======

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')



>>>>>>> a83d2d578620aae3f409aba2a4e17a0ec48f0334
