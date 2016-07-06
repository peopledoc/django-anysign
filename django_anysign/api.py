"""Declaration of API shortcuts.

Everything declared (or imported) in this module is exposed in
:mod:`django_anysign.api` package, i.e. available when one does
``from django_anysign import api as django_anysign``.

Here are the motivations of such an "api" module:

* as a `django-anysign` library user, in order to use `django-anysign`, I just
  do ``from django_anysign import api as django_anysign``.
  It is enough for most use cases. I do not need to bother with more
  `django_anysign` internals. I know this API will be maintained, documented,
  and not deprecated/refactored without notice.

* as a `django-anysign` library developer, in order to maintain
  `django-anysign` API, I focus on things declared in
  :mod:`django_anysign.api`. It is enough. It is required. I take care of this
  API. If there is a change in this API between consecutive releases, then I
  use :class:`DeprecationWarning` and I mention it in release notes.

It also means that things not exposed in :mod:`django_anysign.api` are not part
of the deprecation policy. They can be moved, changed, removed without notice.

"""
from django_anysign.backend import SignatureBackend  # NoQA
from django_anysign.loading import get_signature_backend  # NoQA
from django_anysign.loading import get_signature_type_model  # NoQA
from django_anysign.loading import get_signature_model  # NoQA
from django_anysign.loading import get_signer_model  # NoQA
from django_anysign.models import SignatureType  # NoQA
from django_anysign.models import SignatureFactory  # NoQA
from django_anysign.models import SignerFactory  # NoQA
