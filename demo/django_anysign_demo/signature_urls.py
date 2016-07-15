from django.conf.urls import url
from django.views.generic import TemplateView

from django_anysign_demo import views


signer_view = views.SignerView.as_view()
return_view = TemplateView.as_view(template_name='signer_return.html')
callback_view = TemplateView.as_view(template_name='callback.html')


urlpatterns = [
    url(r'signer/(?P<pk>[0-9]+)/$', signer_view, name='signer'),
    url(r'signer/(?P<pk>[0-9]+)/return/$', return_view, name='signer_return'),
    url(r'callback/(?P<pk>[0-9]+)/$', callback_view, name='callback'),
]
