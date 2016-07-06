import logging

from django import forms
from django.views.generic import FormView, UpdateView

import django_anysign


logger = logging.getLogger(__name__)


class SendView(FormView):
    form_class = forms.Form
    template_name = 'send.html'

    def form_valid(self, form):
        # Create signature instance in local DB.
        SignatureType = django_anysign.get_signature_type_model()
        Signature = django_anysign.get_signature_model()
        Signer = django_anysign.get_signer_model()
        signature_type, created = SignatureType.objects.get_or_create(
            signature_backend_code='dummysign')
        signature = Signature.objects.create(signature_type=signature_type)
        Signer.objects.create(signature=signature)
        logger.debug(
            '[django_anysign_demo] Signature ID={id} created in local DB'
            .format(id=signature.id))
        # Register signature in backend's DB.
        signature.signature_backend.create_signature(signature)
        # Remember the signature object for later use (:meth:`get_success_url`)
        self.signature = signature
        # Handle the form as always.
        return FormView.form_valid(self, form)

    def get_success_url(self):
        backend = self.signature.signature_backend
        signer = self.signature.signers.all()[0]
        return backend.get_signer_url(signer)


class SignerForm(forms.ModelForm):
    """A noop (but pass) model form."""
    class Meta:
        model = django_anysign.get_signer_model()
        fields = []

    def is_valid(self):
        return True

    def save(self, commit=True):
        return self.instance


class SignerView(UpdateView):
    form_class = SignerForm
    template_name = 'signer.html'

    def get_queryset(self):
        Signer = django_anysign.get_signer_model()
        return Signer.objects.all()

    def get_success_url(self):
        backend = self.object.signature_backend
        return backend.get_signer_return_url(self.object)
