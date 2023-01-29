from decouple import config

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

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID", cast=str)

AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY", cast=str)

AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME", cast=str)

AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.us-east-2.amazonaws.com"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = f"{AWS_S3_CUSTOM_DOMAIN}/media/"

MIDDLEWARE.insert(
    1,
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

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

EMAIL_HOST = config("EMAIL_HOST")

EMAIL_HOST_USER = config("EMAIL_HOST_USER")

EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

EMAIL_PORT = 587

EMAIL_USE_TLS = True

SECURE_SSL_REDIRECT = True
