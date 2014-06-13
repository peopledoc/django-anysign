import django_anysign


class DummySignBackend(django_anysign.SignatureBackend):
    def __init__(self):
        super(DummySignBackend, self).__init__(
            name='DummySign',
            code='dummysign',
        )
