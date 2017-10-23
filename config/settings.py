import os

from unipath import Path
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    """Get the environment variable or return exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)

ROOT_DIR = Path(__file__).ancestor(2)

PROJECT_DIR = ROOT_DIR.child('gameboyz')

SECRET_KEY = get_env_variable("SECRET_KEY")
EBAY_APP_ID = get_env_variable("EBAY_APP_ID",)

DEBUG = True

ALLOWED_HOSTS = ['dev.ravedave.co', 'www.dev.ravedave.co']

LOCAL_APPS = [
    'gameboyz.core',
    'gameboyz.consoles',
    'gameboyz.games',
    'gameboyz.accessories',
    'gameboyz.sales',
]

DJANGO_APPS = [
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_celery_beat',
    'django_celery_results',
    'debug_toolbar',
]

INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS

LOGIN_REDIRECT_URL = '/gameboyz'
LOGIN_URL = '/gameboyz'
ACCOUNT_LOGOUT_REDIRECT_URL = '/gameboyz'

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

DEFAULT_FROM_EMAIL = "ravedave@gameboyz.co"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.sendgrid.com"
EMAIL_HOST_USER = "ackleyd1"
EMAIL_MAIN = "ackleyd1@msu.edu"
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_PASSWORD")
EMAIL_PORT = 587
EMAIL_USER_TLS = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR.child('templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gameboyz',
        'USER': 'ackleyd1',
        'PASSWORD': get_env_variable("POSTGRES_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = 'http://dev.ravedave.co/gameboyz/static/'
STATIC_ROOT = PROJECT_DIR.child('static')

MEDIA_URL = 'http://dev.ravedave.co/gameboyz/media/'
MEDIA_ROOT = PROJECT_DIR.child('media')


BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

BRAINTREE_MERCHANT_ID = get_env_variable("BRAINTREE_MERCHANT_ID")
BRAINTREE_PUBLIC_KEY = get_env_variable("BRAINTREE_PUBLIC_KEY")
BRAINTREE_PRIVATE_KEY = get_env_variable("BRAINTREE_PRIVATE_KEY")

def show_toolbar(request):
    if request.user and request.user.username == 'ravedave':
        return True
    return False

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'config.settings.show_toolbar',
}