"""Malenovska URL paths config."""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^$', include('news.urls')),
    url(r'^index/$', include('news.urls')),
    url(r'^register/$', include('registration.urls')),
    url(r'^world/$', include('world.urls')),
    url(r'^info/$', include('info.urls')),
    url(r'^rules/$', include('rules.urls')),
    url(r'^legends/$', include('legends.urls'))
]
