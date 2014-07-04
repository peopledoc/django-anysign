from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_anysign.loading import get_signature_backend_instance


def signature_backend_choices():
    """Return choices for available backends."""
    return [(code, code) for code in settings.ANYSIGN['BACKENDS'].keys()]


class SignatureTypeMixin(models.Model):
    signature_backend_code = models.CharField(
        _('signature backend'),
        max_length=100,
        choices=signature_backend_choices(),
    )

    class Meta:
        abstract = True

    @property
    def signature_backend_options(self):
        """Return dictionary for backend's specific configuration.

        Default implementation returns empty dictionary.

        There are 2 main ways for you to setup backends with the right
        arguments:

        * in the model subclassing this one, override this property. This is
          the good option if you can have several SignatureType instances for
          one backend (:attr:`signature_backend_code` is not unique).

        * in the backend subclass, make ``__init__()`` read the Django
          settings or environment. This can be a good option if you have an
          unique SignatureBackend instance matching a backend
          (:attr:`signature_backend_code` is unique).

        """
        return {}

    def get_signature_backend(self):
        """Instanciate and return signature backend instance."""
        return get_signature_backend_instance(
            self.signature_backend_code,
            **self.signature_backend_options)

    @property
    def signature_backend(self):
        """Return backend from internal cache or new instance.

        If :attr:`signature_backend_code` changed since the last access, then
        the internal (instance level) cache is invalidated and a new instance
        is returned.

        """
        try:
            if self._signature_backend.code != self.signature_backend_code:
                raise AttributeError
            return self._signature_backend
        except AttributeError:
            self._signature_backend = self.get_signature_backend()
            return self._signature_backend


def SignatureMixin(SignatureType):
    class SignatureMixin(models.Model):
        #: Type of the signature, including backend.
        signature_type = models.ForeignKey(
            SignatureType,
            verbose_name=_('signature type'))
        #: Identifier in backend's database.
        signature_backend_id = models.CharField(
            _('ID for signature backend'),
            max_length=100,
            db_index=True,
            blank=True,
            default=u'')

        class Meta:
            abstract = True

        @property
        def signature_backend(self):
            """Return signature backend instance."""
            return self.signature_type.signature_backend

        def signature_documents(self):
            """Return list of documents (file wrappers) to sign.

            The following properties are expected for returned items:

            * ``name``
            * ``bytes``: binary bytes.
              Typically ``lambda x: x.open('rb').read()``

            """
            raise NotImplementedError
    return SignatureMixin


def SignerMixin(Signature):
    class SignerMixin(models.Model):
        signature = models.ForeignKey(
            Signature,
            related_name='signers')

        class Meta:
            abstract = True

        @property
        def signature_backend(self):
            """Return signature backend instance."""
            return self.signature.signature_backend
    return SignerMixin
