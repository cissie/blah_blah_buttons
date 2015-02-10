from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from blahblahbuttons import views
from shop import urls as shop_urls
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blahblahbuttons/', include('blahblahbuttons.urls')),
    url(r'^shop/', include('shop.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
