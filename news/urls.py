from django.conf.urls import url

from .views import NewsView

urlpatterns = [
    url(r'^$', NewsView.as_view(), name='index')
]
