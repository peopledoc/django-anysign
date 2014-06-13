# -*- coding: utf-8 -*-
"""Django settings for django-anysign demo project."""
from os.path import abspath, dirname, join


# Configure some relative directories.
demoproject_dir = dirname(abspath(__file__))
demo_dir = dirname(demoproject_dir)
root_dir = dirname(demo_dir)
data_dir = join(root_dir, 'var')
cfg_dir = join(root_dir, 'etc')


# Mandatory settings.
ROOT_URLCONF = 'django_anysign_demo.urls'
WSGI_APPLICATION = 'django_anysign_demo.wsgi.application'


# Database.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(data_dir, 'db.sqlite'),
    }
}


# Required.
SECRET_KEY = "This is a secret made public on project's repository."

# Media and static files.
MEDIA_ROOT = join(data_dir, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = join(data_dir, 'static')
STATIC_URL = '/static/'


# Applications.
INSTALLED_APPS = (
    # The actual django-anysign demo.
    'django_anysign_demo',
    # Third-parties.
    'south',
    # Standard Django applications.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Stuff that must be at the end.
    'django_nose',
)


ANYSIGN = {
    'BACKENDS': {
        'dummysign': 'django_dummysign.backend.DummySignBackend',
    },
    'SIGNATURE_TYPE_MODEL': 'django_anysign_demo.models.SignatureType',
    'SIGNATURE_MODEL': 'django_anysign_demo.models.Signature',
    'SIGNER_MODEL': 'django_anysign_demo.models.Signer',
}


# Test/development settings.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
nose_cfg_dir = join(cfg_dir, 'nose')
NOSE_ARGS = [
    '--verbosity=2',
    '--no-path-adjustment',
    '--nocapture',
    '--all-modules',
    '--rednose',
]
