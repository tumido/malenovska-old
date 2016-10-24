from django.conf.urls import url

from .views import WorldView

urlpatterns = [
    url(r'^$', WorldView.as_view(), name='index')
]
