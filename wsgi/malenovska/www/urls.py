
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    #url(r'^race/(?P<race_name>[a-zA-Z]+)$', views.RaceView.as_view, name='race'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^world/$', views.WorldView.as_view(), name='world'),
    url(r'^info/$', views.InfoView.as_view(), name='info'),
    url(r'^legends/$', views.LegendView.as_view(), name='legends')
]
