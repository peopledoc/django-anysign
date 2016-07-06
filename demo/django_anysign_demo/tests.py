# coding=utf8
"""Test suite for demoproject.download."""
from django.core.urlresolvers import reverse
from django.test import TestCase

import django_anysign


class HomeURLTestCase(TestCase):
    """Test homepage."""
    def test_get(self):
        """Homepage returns HTTP 200."""
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class SendURLTestCase(TestCase):
    """Test "create and send signature" view."""
    def test_get(self):
        """GET "send" URL returns HTTP 200."""
        url = reverse('send')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        """POST "send" URL creates a signature and redirects to signer view."""
        Signature = django_anysign.get_signature_model()
        self.assertEqual(Signature.objects.all().count(), 0)
        url = reverse('send')
        response = self.client.post(url)
        self.assertEqual(Signature.objects.all().count(), 1)
        signature = Signature.objects.get()
        signer = signature.signers.all()[0]
        signer_url = signature.signature_backend.get_signer_url(signer)
        self.assertRedirects(response, signer_url)


class SignerURLTestCase(TestCase):
    """Test "create and send signature" view."""
    def test_get(self):
        """GET "anysign:signer" URL returns HTTP 200."""
        # Create a signature.
        SignatureType = django_anysign.get_signature_type_model()
        Signature = django_anysign.get_signature_model()
        Signer = django_anysign.get_signer_model()
        signature_type, created = SignatureType.objects.get_or_create(
            signature_backend_code='dummysign')
        signature = Signature.objects.create(signature_type=signature_type)
        signer = Signer.objects.create(signature=signature)
        signature.signers.add(signer)

        url = reverse('anysign:signer', args=[signer.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        """POST "anysign:signer" URL redirects to "signer return"."""
        # Create a signature.
        SignatureType = django_anysign.get_signature_type_model()
        Signature = django_anysign.get_signature_model()
        Signer = django_anysign.get_signer_model()
        signature_type, created = SignatureType.objects.get_or_create(
            signature_backend_code='dummysign')
        signature = Signature.objects.create(signature_type=signature_type)
        signer = Signer.objects.create(signature=signature)

        url = reverse('anysign:signer', args=[signer.pk])
        response = self.client.post(url, follow=True)
        signer_return_url = signature.signature_backend.get_signer_return_url(
            signer)
        self.assertEqual(
            signer_return_url,
            reverse('anysign:signer_return', args=[signer.pk])
        )
        self.assertRedirects(response, signer_return_url)
        self.assertEqual(response.status_code, 200)
