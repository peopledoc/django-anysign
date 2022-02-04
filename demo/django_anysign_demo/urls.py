from django.urls import include, path
from django.views.generic import TemplateView

from django_anysign_demo import views


home_view = TemplateView.as_view(template_name='home.html')
send_view = views.SendView.as_view()


urlpatterns = [
    path(
        'signature/',
        include('django_anysign_demo.signature_urls', namespace='anysign')
    ),
    path('send/', send_view, name='send'),
    path('', home_view, name='home')
]
