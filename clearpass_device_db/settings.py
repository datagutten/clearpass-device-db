"""
Django settings for clearpass_device_db project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
import urllib.parse

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
try:
    import dotenv

    dotenv.load_dotenv(BASE_DIR.absolute() / '.env')
except ImportError:
    dotenv = None
    pass

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = bool(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
if os.getenv('DOMAIN').find('http') != 0:
    base_url = "https://%s" % os.getenv('DOMAIN')
else:
    base_url = os.getenv('DOMAIN')

if os.environ.get("DJANGO_ALLOWED_HOSTS"):
    ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
else:
    parts = urllib.parse.urlparse(base_url)
    ALLOWED_HOSTS = [parts.hostname]

if os.environ.get("CSRF_TRUSTED_ORIGINS"):
    CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")
else:
    CSRF_TRUSTED_ORIGINS = [base_url]


# Application definition

INSTALLED_APPS = [
    "devices.apps.DevicesConfig",
    "device_selfservice.apps.DeviceSelfserviceConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_bootstrap5",
    "azure_auth",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "azure_auth.middleware.AzureMiddleware",
]

ROOT_URLCONF = "clearpass_device_db.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "clearpass_device_db.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "3306"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = os.getenv("TZ", "UTC")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# MACADDRESS_DEFAULT_DIALECT = 'netaddr.mac_bare'
MACADDRESS_DEFAULT_DIALECT = 'devices.mac_lower'

AZURE_AUTH = {
    "CLIENT_ID": os.getenv('MS_CLIENT_ID'),
    "CLIENT_SECRET": os.getenv('MS_CLIENT_SECRET'),
    "REDIRECT_URI": "%s/azure_auth/callback" % base_url,
    "SCOPES": ["User.Read"],
    "AUTHORITY": "https://login.microsoftonline.com/common",
    "PUBLIC_URLS": ["index"],  # Optional, public views accessible by non-authenticated users
    "USERNAME_ATTRIBUTE": "userPrincipalName",   # The AAD attribute or ID token claim you want to use as the value for the user model `USERNAME_FIELD`
    # "EXTRA_FIELDS": [], # Optional, extra AAD user profile attributes you want to make available in the user mapping function
    # "USER_MAPPING_FN": "azure_auth.tests.misc.user_mapping_fn", # Optional, path to the function used to map the AAD to Django attributes
}
LOGIN_URL = "/azure_auth/login"
LOGIN_REDIRECT_URL = "/"    # Or any other endpoint
AUTHENTICATION_BACKENDS = ("azure_auth.backends.AzureBackend",)
