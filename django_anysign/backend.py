"""Base material for signature backends."""
from django.core.urlresolvers import reverse


class SignatureBackend(object):
    """Encapsulate signature workflow and integration with vendor backend.

    Here is a typical workflow:

    * :class:`~django_anysign.models.SignatureType` instance is created. It
      encapsulates the backend type and its configuration.

    * A :class:`~django_anysign.models.Signature` instance is created.
      The signature instance has a signature type attribute, hence a backend.

    * Signers are notified, by email, text or whatever. They get an hyperlink
      to the "signer view". The URL may vary depending on the signature
      backend.

    * A signer goes to the backend's "signer view" entry point: typically a
      view that integrates backend specific form to sign a document.

    * Most backends have a "notification view", for the third-party service to
      signal updates.

    * Most backends have a "signer return view", where the signer is redirected
      when he ends the signature process (whatever signature status).

    * The backend's specific workflow can be made of several views. At the
      beginning, there is a Signature instance which carries data (typically a
      document). At the end, Signature is done.

    """
    def __init__(self, name, code):
        """Configure backend."""
        #: Human-readable name.
        self.name = name

        #: Machine-readable name. Should be lowercase alphanumeric only, i.e.
        #: PEP-8 compliant.
        self.code = code

    def send_signature(self, signature):
        """Initiate the signature process.

        At this state, the signature object has been configured.

        Typical implementation consists in sending signer URL to first signer.

        Raise ``NotImplementedError`` if the backend does not support such a
        feature.

        """
        raise NotImplementedError()

    def get_signer_url(self, signer):
        """Return URL where signer signs document.

        Raise ``NotImplementedError`` in case the backend does not support
        "signer view" feature.

        Default implementation reverses :meth:`get_signer_url_name` with
        ``signer.pk`` as argument.

        """
        return reverse(self.get_signer_url_name(), args=[signer.pk])

    def get_signer_url_name(self):
        """Return URL name where signer signs document.

        Raise ``NotImplementedError`` in case the backend does not support
        "signer view" feature.

        Default implementation returns ``anysign:signer``.

        """
        return 'anysign:signer'

    def get_signer_return_url(self, signer):
        """Return URL where signer is redirected once document has been signed.

        Raise ``NotImplementedError`` in case the backend does not support
        "signer return view" feature.

        Default implementation reverses :meth:`get_signer_return_url_name`
        with ``signer.pk`` as argument.

        """
        return reverse(
            self.get_signer_recipient_url_name(),
            args=[signer.pk])

    def get_signer_return_url_name(self):
        """Return URL name where signer is redirected once document has been
        signed.

        Raise ``NotImplementedError`` in case the backend does not support
        "signer return view" feature.

        Default implementation returns ``anysign:signer_return``.

        """
        return 'anysign:signer_return'

    def get_signature_callback_url(self, signature):
        """Return URL where backend can post signature notifications.

        Raise ``NotImplementedError`` in case the backend does not support
        "signature callback url" feature.

        Default implementation reverses :meth:`get_signature_callback_url_name`
        with ``signature.pk`` as argument.

        """
        return reverse(
            self.get_signature_callback_url_name(),
            args=[signature.pk])

    def get_signature_callback_url_name(self):
        """Return URL name where backend can post signature notifications.

        Raise ``NotImplementedError`` in case the backend does not support
        "signer return view" feature.

        Default implementation returns ``anysign:signature_callback``.

        """
        return 'anysign:signature_callback'
