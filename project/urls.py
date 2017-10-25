"""Malenovska URL paths config."""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^index/', include('news.urls')),
    url(r'^register/', include('registration.urls')),
    url(r'^world/', include('world.urls')),
    url(r'^info/', include('info.urls')),
    url(r'^rules/', include('rules.urls')),
    url(r'^legends/', include('legends.urls')),
    url(r'^health', include('health_check.urls')),
    url(r'^', include('news.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
