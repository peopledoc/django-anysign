"""Specific settings for `django-anysign`."""
from django.conf import settings


ANYSIGN = {
    'BACKENDS': {},
    'SIGNATURE_TYPE_MODEL': None,
    'SIGNATURE_MODEL': None,
    'SIGNER_MODEL': None,
}
if not hasattr(settings, 'ANYSIGN'):
    setattr(settings, 'ANYSIGN', ANYSIGN)
