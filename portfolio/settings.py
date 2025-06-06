"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import environ
import os
from django.utils.translation import ugettext_lazy as _
from my_secrets import secrets

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = env('DEBUG')

ALLOWED_HOSTS =  ['*']

# Application definition

INSTALLED_APPS = [
    'mainpage.apps.MainpageConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_secrets',
    'cookiebanner',
    'hitcount',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': secrets.DBNAME,
        'USER': secrets.DBUSER,
        'PASSWORD': secrets.DBPASSWORD,
        'HOST': secrets.DBHOST,
        'PORT': secrets.DBPORT,
        'OPTIONS': {'sql_mode': 'STRICT_TRANS_TABLES'},
    },
    'extra': env.db_url(
        'SQLITE_URL',
        default='sqlite:////tmp/tmp-sqlite.db'
    )
}

try:
    if env('ENVIRONMENT') == 'DEV':
        DATABASES['default'] = DATABASES['extra']
except environ.ImproperlyConfigured:
    pass

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGES = (
        ('en', _('English')),
        ('es', _('Spanish')),
)

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

#USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/staticfiles/'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

try:
    if env('ENVIRONMENT') == 'DEV':
        STATIC_ROOT = ''    # It MUST be empty with manage runserver
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'portfolio', 'staticfiles'),
        ]
except environ.ImproperlyConfigured:
    pass

# For sending emails
EMAIL_USE_TLS = True
EMAIL_HOST = secrets.EMAIL_HOST
EMAIL_HOST_USER = secrets.EMAIL_USER
EMAIL_HOST_PASSWORD = secrets.EMAIL_PASSWORD
EMAIL_PORT = 587

# RGPD cookie banner
COOKIEBANNER = {
    "title": _("Cookie settings"),
    "header_text": _("This website uses optional cookies for usability purposes. It does not collect any personal data."),
    "footer_text": _("Essential cookies are used for proper functioning and can't be declined."),
    "footer_links": [
        {"title": _("AEPD"), "href": "https://www.aepd.es/es"},
        {"title": _("GDPR"), "href": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02016R0679-20160504"},
    ],
    "groups": [
        {
            "id": "essential",
            "name": _("Essential"),
            "description": _("Essential cookies allow this page to work."),
            "cookies": [
                {
                    "pattern": "cookiebanner",
                    "description": _("Meta cookie for the cookies that are set."),
                },
                {
                    "pattern": "csrftoken",
                    "description": _("This cookie prevents Cross-Site-Request-Forgery attacks."),
                },
                {
                    "pattern": "sessionid",
                    "description": _("This cookie is necessary to allow logging in, for example."),
                },
            ],
        },
        {
            "id": "preferences",
            "name": _("Preferences"),
            "optional": True,
            "cookies": [
                {
                    "pattern": "django_language",
                    "description": _("Allows to display webpage in selected language and remember on next visits."),
                },
            ],
        },
    ],
}

