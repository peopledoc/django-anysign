from django.conf.urls import include, url
from django.views.generic import TemplateView

from django_anysign_demo import views


home_view = TemplateView.as_view(template_name='home.html')
send_view = views.SendView.as_view()


urlpatterns = [
    url(r'^signature/',
        include('django_anysign_demo.signature_urls',
                app_name='anysign',
                namespace='anysign')),
    url(r'^send/$', send_view, name='send'),
    url(r'^$', home_view, name='home')
]
