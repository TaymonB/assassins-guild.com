"""
Django settings for assassins_guild project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

import environ

root = environ.Path(__file__) - 2
env = environ.Env()
if 'DATABASE_URL' not in os.environ:
    environ.Env.read_env(root('.env'))

# Development vs. production mode
DEBUG = TEMPLATE_DEBUG = env('DEBUG', bool, False)

# Database
DATABASES = {'default': env.db()}

# Serving static media files
STATIC_ROOT = root('static/')

# Security
SECRET_KEY = env('SECRET_KEY')
if not DEBUG:
    ALLOWED_HOSTS = env('ALLOWED_HOSTS', list)
    if env('HTTP_X_FORWARDED_PROTO', bool, False):
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Localization, etc.
LANGUAGE_CODE = env('LANGUAGE_CODE')
TIME_ZONE = env('TIME_ZONE')

# The rest of this stuff doesn't depend on deployment settings.

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'assassins_guild.urls'
WSGI_APPLICATION = 'assassins_guild.wsgi.application'

STATIC_URL = 'static/'

if not DEBUG:
    CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE = True

USE_I18N = USE_L10N = USE_TZ = True
