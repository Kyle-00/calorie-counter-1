"""
Django settings for calorie_counter project.
"""

import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------- SECURITY ----------
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-fallback-key')

# Force DEBUG=False in production (set via environment)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# HARDCODE ALLOWED_HOSTS – this eliminates the 400 error
ALLOWED_HOSTS = ['*']   # Accepts any host – change later if you want to restrict

# HARDCODE CSRF trusted origins – required for POST requests on Render
CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com', 'http://*.onrender.com']

# ---------- INSTALLED APPS ----------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'calorie_tracker',
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

ROOT_URLCONF = 'calorie_counter.urls'

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

WSGI_APPLICATION = 'calorie_counter.wsgi.application'

# ---------- DATABASE ----------
if DEBUG:
    # Local development (PostgreSQL on port 5433)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'calorie_db',
            'USER': 'calorie_user',
            'PASSWORD': 'kikikyle2005',
            'HOST': 'localhost',
            'PORT': '5433',
        }
    }
else:
    # Production – read DATABASE_URL from environment
    DATABASES = {
        'default': dj_database_url.config()
    }

# ---------- PASSWORD VALIDATION ----------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------- INTERNATIONALIZATION ----------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------- STATIC FILES ----------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ---------- DEFAULT AUTO FIELD ----------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'