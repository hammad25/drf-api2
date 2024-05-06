"""
Django settings for drf_api2 project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
if os.path.exists('env.py'):
    import env

import re

import environ

# Set up environment variables
env = environ.Env()
# Assuming your .env file is at the same level as manage.py
environ.Env.read_env()

# Now access your environment variable
CLOUDINARY_URL = env('CLOUDINARY_URL')
print("CLOUDINARY_URL:", CLOUDINARY_URL)



# Example of loading the environment variable
# os.environ['CLOUDINARY_URL'] = 'cloudinary://271367374156864:sCF4a2qjC4XGewrp7JFJekYhN-8@dppkcahdz'

cloudinary_url = os.getenv('CLOUDINARY_URL')
if cloudinary_url:
    regex = re.compile(r'^cloudinary://(?P<api_key>[^:]+):(?P<api_secret>[^@]+)@(?P<cloud_name>[^/]+)$')
    match = regex.match(cloudinary_url)
    if match:
        CLOUDINARY_STORAGE = {
            'CLOUD_NAME': match.group('cloud_name'),
            'API_KEY': match.group('api_key'),
            'API_SECRET': match.group('api_secret')
        }
    else:
        raise ValueError("Invalid CLOUDINARY_URL")
else:
    raise ValueError("CLOUDINARY_URL not set")


MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^j8ev9)x7-7)upcma81%zeb$z9ik8q0-#&+_5*g@i#w0=ocgj8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '[::1]',
    '8000-hammad25-drfapi2-fk04a312d4z.ws-eu111.gitpod.io',
    '.gitpod.io',
    '8000-hammad25-drfapi2-fk04a312d4z.ws-eu111.gitpod.io',

]

CSRF_TRUSTED_ORIGINS = ['https://*.gitpod.io']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',

    'profiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drf_api2.urls'

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

WSGI_APPLICATION = 'drf_api2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
