"""
Django settings for violance_analytics project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import dotenv
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# This is new:

import dotenv
DOTENV_FILE = os.path.join(BASE_DIR, ".env")
ENV = False

if os.path.isfile(DOTENV_FILE):
    ENV = True
if ENV:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': dotenv.get_key(DOTENV_FILE, 'DB_NAME'),
            'USER': dotenv.get_key(DOTENV_FILE, 'DB_USER'),
            'PASSWORD': dotenv.get_key(DOTENV_FILE, 'DB_PASSWORD'),
            'HOST': dotenv.get_key(DOTENV_FILE, 'DB_HOST'),
            'PORT': dotenv.get_key(DOTENV_FILE, 'DB_PORT')
        }
    }
else:
    DATABASES = dict()
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-clwfe(9rdf(a%$%uzew=tz=6qj-*s21#kyj1t23ixyeuyv1&l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'violance_analytics.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'violance_analytics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# This should already be in your settings.py
django_heroku.settings(locals())
# This is new
if not ENV:
    del DATABASES['default']['OPTIONS']['sslmode']