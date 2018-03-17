"""Django settings for powersocket project."""

import environ

env = environ.Env(DEBUG=(bool, False),)

BASE_DIR = environ.Path(__file__) - 2
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1', 'powersocket.pythonanywhere.com', '.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'orders',
    'products',
    'userauth',
    'registration',
    'webui'
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

ROOT_URLCONF = 'powersocket.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['webui/templates/main',
                 'webui/templates/registration',
                 'webui/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.count_products_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'powersocket.wsgi.application'


# Database, secret key, debug
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DEBUG = env('DEBUG')


DATABASES = {
    'default': env.db(default='sqlite:///db.sqlite3'),
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT_DIR = env.path('STATIC_ROOT', BASE_DIR('static'))
STATIC_ROOT = STATIC_ROOT_DIR()

MEDIA_URL = '/media/'
MEDIA_ROOT_DIR = env.path('MEDIA_ROOT', BASE_DIR('media'))
MEDIA_ROOT = MEDIA_ROOT_DIR()

# Registration settings
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/'

print(BASE_DIR)
