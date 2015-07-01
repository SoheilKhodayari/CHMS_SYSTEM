"""
Django settings for CHMS project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOGIN_URL = "login_all/"
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
AUTH_PROFILE_MODULE = 'hospital.BaseUser'
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '72=v)f8!^d!b0%mxmc%hfhu(!40lc9&8@loh%222xx4a(98_u-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_messages',
    'history_records',
    'Medical Diagnosis File',
    'hospital',
    'patient',
    'pharmacy',
    'equipment',
    'physician',
    'Receptionist',
    'medicine',
    'androidApp',
    'schedule',
    'nurse',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

# TEMPLATE_LOADERS = (
#     #'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.filesystem',
# )
ROOT_URLCONF = 'CHMS.urls'

WSGI_APPLICATION = 'CHMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#~ DATABASES = {
   #~ 'default': {
       #~ 'ENGINE': 'django.db.backends.sqlite3',
       #~ 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   #~ }
#~ }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'CHMS',
#         'USER': 'root',
#         'PASSWORD': 'soheil',
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }

 DATABASES = {
     'default': {
         'NAME': 'CHMS',
         'ENGINE': 'mysql.connector.django',
         'USER': 'root',
         'PASSWORD': 'soheil',
         'OPTIONS': {
           'autocommit': True,
         },
     }
 }
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
ADMIN_MEDIA_PREFIX = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR,"static")
