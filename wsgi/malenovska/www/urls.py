
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.NewsView.as_view(), name='index'),
    url(r'^index/$', views.NewsView.as_view(), name='index'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^world/$', views.WorldView.as_view(), name='world'),
    url(r'^info/$', views.InfoView.as_view(), name='info'),
    url(r'^rules/$', views.RulesView.as_view(), name='rules'),
    url(r'^legends/$', views.LegendView.as_view(), name='legends')
]
