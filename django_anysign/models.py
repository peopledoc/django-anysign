import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_anysign import settings
from django_anysign.loading import get_signature_backend


def signature_backend_choices():
    """Return choices for available backends."""
    return [(code, code) for code in settings.ANYSIGN['BACKENDS'].keys()]


class SignatureType(models.Model):
    """Abstract base model for signature type.

    A signature type encapsulates backend setup. Typically:

    * a "configured backend" is a backend class (such as
      :class:`~django-dummysign.backend.DummySignBackend`) and related
      configuration (URL, credentials...).

    * a ``Signature`` instance will be related to a configured backend, via a
      ``SignatureType``.

    """
    #: Machine-readable code for the backend.
    #: Typically related to settings, by default keys in
    #: ``settings.ANYSIGN['BACKENDS']`` dictionary.
    signature_backend_code = models.CharField(
        _('signature backend'),
        max_length=50,
        choices=signature_backend_choices(),
        db_index=True,
    )

    class Meta:
        abstract = True

    @property
    def signature_backend_options(self):
        """Dictionary for backend's specific configuration.

        Default implementation returns empty dictionary.

        There are 2 main ways for you to setup backends with the right
        arguments:

        * in the model subclassing this one, override this property. This is
          the good option if you can have several ``SignatureType`` instances
          for one backend, i.e. if :attr:`signature_backend_code` is not
          unique.

        * in the backend's subclass, make ``__init__()`` read the Django
          settings or environment. This can be a good option if you have an
          unique ``SignatureBackend`` instance matching a backend
          (:attr:`signature_backend_code` is unique).

        """
        return {}

    def get_signature_backend(self):
        """Instanciate and return signature backend instance.

        Default implementation uses
        :func:`~django-anysign.loading.get_backend_instance` with
        :attr:`signature_backend_code` as positional arguement and with
        :meth:`signature_backend_options` as keyword arguments.

        """
        return get_signature_backend(
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


def SignatureFactory(SignatureType):
    """Return base class for signature model, using ``SignatureType`` model.

    This pattern is the best one we found at the moment to have an abstract
    base model ``SignatureBase`` with appropriate foreign key to
    ``SignatureType`` model. Feel free to propose a better option if you know
    one ;)

    """
    class Signature(models.Model):
        """Base model for signature models."""
        #: Type of the signature, i.e. a backend and its configuration.
        signature_type = models.ForeignKey(
            SignatureType,
            verbose_name=_('signature type'))

        #: Identifier in backend's external database.
        signature_backend_id = models.CharField(
            _('ID for signature backend'),
            max_length=100,
            db_index=True,
            blank=True,
            default=u'')

        #: Identifier in Django's internal database.
        anysign_internal_id = models.UUIDField(
            verbose_name=_('ID in internal database'),
            default=uuid.uuid4)

        class Meta:
            abstract = True

        @property
        def signature_backend(self):
            """Signature backend instance.

            This is just an utility shortcut, an alias to signature type's
            backend property.

            """
            return self.signature_type.signature_backend

        def signature_documents(self):
            """Return list of documents (file wrappers) to sign.

            The following properties are expected for returned items:

            * ``name``
            * ``bytes``: binary bytes.
              Typically ``lambda x: x.open('rb').read()``

            Default implementation raises :class:`NotImplementedError`, i.e.
            your custom signature class must override this method.

            """
            raise NotImplementedError
    return Signature


def SignerFactory(Signature):
    """Return base class for signer model, using ``Signature`` model.

    This pattern is the best one we found at the moment to have an abstract
    base model ``Signer`` with appropriate foreign key to ``Signature``
    model. Feel free to propose a better option if you know one ;)

    """
    class Signer(models.Model):
        """Base class for signer.

        A signer is typically related to an user... but could be anything you
        want! By default, it is just related to a signature.

        """
        #: Signature.
        signature = models.ForeignKey(
            Signature,
            related_name='signers')

        #: Position as a signer.
        signing_order = models.PositiveSmallIntegerField(
            _('signing order'),
            default=0,
            help_text=_('Position in the list of signers.'))

        #: Identifier in backend's external database.
        signature_backend_id = models.CharField(
            _('ID in signature backend'),
            max_length=100,
            db_index=True,
            blank=True,
            default=u'')

        #: Identifier in Django's internal database.
        anysign_internal_id = models.UUIDField(
            verbose_name=_('ID in internal database'),
            default=uuid.uuid4)

        class Meta:
            abstract = True

        @property
        def signature_backend(self):
            """Signature backend instance.

            This is just an utility shortcut, an alias to signature type's
            backend property.

            """
            return self.signature.signature_backend

        def get_absolute_url(self):
            return self.signature_backend.get_signer_url(self)
    return Signer
