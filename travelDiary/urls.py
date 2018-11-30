from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 


if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^beaches/', include('beaches.urls')),
    url(r'^food/', include('food.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
