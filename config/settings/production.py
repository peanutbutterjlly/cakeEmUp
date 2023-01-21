import os

from .base import *

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.us-east-2.amazonaws.com"

STATIC_URL = f"{AWS_S3_CUSTOM_DOMAIN}/static/"

STATICFILES_STORAGE = "cake_order_project.backends.StaticStorage"

MEDIA_URL = f"{AWS_S3_CUSTOM_DOMAIN}/media/"

DEFAULT_FILE_STORAGE = "cake_order_project.backends.MediaStorage"

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DB_NAME", cast=str),
        "USER": config("DB_USER", cast=str),
        "PASSWORD": config("DB_PASSWORD", cast=str),
        "HOST": config("DB_HOST", cast=str),
    }
}

SECURE_SSL_REDIRECT = True
