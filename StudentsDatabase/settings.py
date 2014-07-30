"""
Django settings for StudentsDatabase project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4veq!sp(=8(51u3j7ok4o1(cmcgmt!hhs15&uil0$1iktg8=ee'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'StudentsListing',
    'bootstrapform', #pip install django-bootstrap-form
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'StudentsListing.middlewares.QueryStatistics',
)

AUTHENTICATION_BACKENDS = (
    'StudentsListing.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'StudentsListing.context_processor.context_settings',
)

ROOT_URLCONF = 'StudentsDatabase.urls'

WSGI_APPLICATION = 'StudentsDatabase.wsgi.application'

ACCOUNT_ACTIVATION_DAYS  = 7

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = rel('..', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    rel('static'),
)

TEMPLATE_DIRS = (
    rel('templates')
)