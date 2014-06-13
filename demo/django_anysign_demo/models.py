import django_anysign.models


class SignatureType(django_anysign.models.SignatureTypeMixin):
    pass


class Signature(django_anysign.models.SignatureMixin(SignatureType)):
    pass


class Signer(django_anysign.models.SignerMixin(Signature)):
    pass
