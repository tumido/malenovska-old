from django.conf.urls import url

from .views import RulesView

urlpatterns = [
    url(r'^$', RulesView.as_view(), name='index')
]
