from django.urls import path
from django.views.generic import TemplateView

from django_anysign_demo import views


app_name = 'anysign'

signer_view = views.SignerView.as_view()
return_view = TemplateView.as_view(template_name='signer_return.html')
callback_view = TemplateView.as_view(template_name='callback.html')

urlpatterns = [
    path('signer/<int:pk>/', signer_view, name='signer'),
    path('signer/<int:pk>/return/', return_view, name='signer_return'),
    path('callback/<int:pk>/', callback_view, name='callback'),
]
