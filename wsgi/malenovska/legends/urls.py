from django.conf.urls import url

from .views import LegendView

urlpatterns = [
    url(r'^$', LegendView.as_view(), name='index')
]
