from django.conf.urls import url
from badige.views import best_marketing

urlpatterns = [
    url(r'roi/(?P<year>[0-9]{4})/(?P<quarter>\d{1})/$', best_marketing),
    ]
