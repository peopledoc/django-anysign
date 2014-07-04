import logging

import django_anysign


logger = logging.getLogger(__name__)


class DummySignBackend(django_anysign.SignatureBackend):
    def __init__(self):
        super(DummySignBackend, self).__init__(
            name='DummySign',
            code='dummysign',
        )

    def create_signature(self, signature):
        """Register ``signature`` in backend, return updated object.

        As a dummy backend: just emit a log.

        """
        signature = super(DummySignBackend, self).create_signature(self)
        logger.debug('[django_dummysign] Signature created in backend')
        return signature
