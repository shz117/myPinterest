"""
Django settings for MyPinterest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PICTURE_DIR = os.path.join(BASE_DIR, 'MyPinterest/Picture/media/pictures')

#DB settings:


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wamotamx&+x7bte%4$)j+xp#9c))__#np5#&fro!56xss+2c-_'

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
    #'MyPinterestApp',
    'MyPinterest.User',
    'MyPinterest.Picture',
    'MyPinterest.Pinboard',
    'MyPinterest.Relations',
    #3rd party friendship
    'friendship',
    'django.contrib.admin',
    'south',
    'django.contrib.sites',
    #comments 3rd party
    'threadedcomments',
    'django.contrib.comments',
)

# to use threadedcomments
COMMENTS_APP = 'threadedcomments'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MyPinterest.urls'

WSGI_APPLICATION = 'MyPinterest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pi2',
        'USER': 'root',
        'HOST':'localhost',
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

STATIC_URL = '/static/'

#AUTHENTICATION_BACKENDS = (
#    'MyPinterestApp.UserManager.auth_backends.PiUserModelBackend',
#)
#
#Pi_USER_MODEL = 'accounts.PiUser'
print BASE_DIR
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'MyPinterest/User/templates')
)

AUTH_USER_MODEL='User.User'