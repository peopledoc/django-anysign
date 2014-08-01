"""Utilities to load custom stuff for signatures."""
from django.conf import settings

from django_anysign.utils.importlib import import_member


def get_signature_backend_instance(code, *args, **kwargs):
    """Instantiate instance for ``backend_code``."""
    factory_path = settings.ANYSIGN['BACKENDS'][code]
    factory = import_member(factory_path)
    return factory(*args, **kwargs)


def get_model(setting):
    """Import and return the model class by ``settings.ANYSIGN[{setting}]``."""
    model_path = settings.ANYSIGN[setting]
    model = import_member(model_path)
    return model


def get_signature_type_model():
    """Return model defined as ``settings.ANYSIGN['SIGNATURE_TYPE_MODEL']``."""
    return get_model('SIGNATURE_TYPE_MODEL')


def get_signature_model():
    """Return model defined as ``settings.ANYSIGN['SIGNATURE_MODEL']``."""
    return get_model('SIGNATURE_MODEL')


def get_signer_model():
    """Return model defined as ``settings.ANYSIGN['SIGNER_MODEL']``."""
    return get_model('SIGNER_MODEL')
