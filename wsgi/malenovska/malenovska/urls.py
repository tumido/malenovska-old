"""Malenovska URL paths config."""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('www.urls')),
    # url(r'^about$', 'www.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
]
