from django.conf.urls import url

from .views import InfoView

urlpatterns = [
    url(r'^$', InfoView.as_view(), name='index')
]
