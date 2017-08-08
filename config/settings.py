import os

from unipath import Path

ROOT_DIR = Path(__file__).ancestor(2)

PROJECT_DIR = ROOT_DIR.child('gameboyz')

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

CONSOLES = {
    'Nintendo Entertainment System (NES)': 18,
    'Super Nintendo Entertainment System (SNES)': 19,
    'Nintendo 64': 4,
    'Nintendo GameCube': 21,
    'Game Boy': 33,
    'Game Boy Color': 22,
    'Game Boy Advance': 24,
}

SECRET_KEY = os.environ["SECRET_KEY"]
PRICE_CHARTING_TOKEN = os.environ["PRICE_CHARTING_TOKEN"]

IGDB_MASHAPE_URL = "https://igdbcom-internet-game-database-v1.p.mashape.com"
X_MASHAPE_KEY = os.environ["X_MASHAPE_KEY"]
EBAY_APP_ID = os.environ["EBAY_APP_ID"]

DEBUG = True

ALLOWED_HOSTS = ['dev.ravedave.co', 'www.dev.ravedave.co']

# Application definition

INSTALLED_APPS = [
    'gameboyz.core',
    'gameboyz.consoles',
    'gameboyz.games',
    'gameboyz.accessories',
    'gameboyz.sales',
    'rest_framework',
    'debug_toolbar',

    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'crispy_forms',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/gameboyz'
ACCOUNT_LOGOUT_REDIRECT_URL = '/gameboyz'

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v2.4',
    }
}

EMAIL_HOST = "smtp.sendgrid.com"
EMAIL_HOST_USER = "ackleyd1"
EMAIL_MAIN = "ackleyd1@msu.edu"
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_PORT = 587
EMAIL_USER_TLS = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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
        'PASSWORD': os.environ["POSTGRES_PASSWORD"],
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

STATIC_URL = '/gameboyz/static/'
STATIC_ROOT = PROJECT_DIR.child('static')

MEDIA_URL = '/gameboyz/media/'
MEDIA_ROOT = PROJECT_DIR.child('media')
