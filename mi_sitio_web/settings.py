"""
Django settings for mi_sitio_web project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eh8k%=-=$53lxb_*j&p9^y8gced!3snkm3-rf*256ryj3+w%ju'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'senderos.apps.SenderosConfig',
    'rest_framework',
    'corsheaders'
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],    
}

ROOT_URLCONF = 'mi_sitio_web.urls'

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

WSGI_APPLICATION = 'mi_sitio_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

import mongoengine
mongoengine.connect(db='senderos_db', host='mongo', username='', password='')

DATABASES = {
#     'default' : {
#        'ENGINE' : 'django.db.backends.dummy',
#        'NAME' : 'senderos_db'
#     }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #{
    #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOG_FILE = os.path.join(BASE_DIR, 'Server.log')

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
				
	'formatters': {
		'verbose': {
			'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
									'datefmt': "%d/%b/%Y %H:%M:%S"
							},
		'simple': {
			'format': '%(levelname)s [%(name)s:%(lineno)s] %(message)s'
							},
						},
				
	'handlers': {
		'file': {
			'level': 'INFO',
			'class': 'logging.FileHandler',
			'filename': os.path.join(BASE_DIR, LOG_FILE),
			'formatter': 'verbose',
			'mode': 'w'
			},
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'simple'
		}
	},
				
	'loggers': {
		'django': {
			'handlers': ['file'],
			'propagate': True,
			'level': 'ERROR',
		},
		'': {
				'handlers': ['file', 'console'],
				'level': 'DEBUG',
			}
		}
	}	