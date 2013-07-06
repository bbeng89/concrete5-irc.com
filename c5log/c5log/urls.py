from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('c5messages.urls')),
    url(r'^', include('staticpages.urls')),
    url(r'^', include('membership.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
