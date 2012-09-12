from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rootapp.views.home', name='home'),
    # url(r'^rootapp/', include('rootapp.foo.urls')),
    
    (r'^accounts/', include('allauth.urls')),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html' }),
    url(r'^accounts/profile/$', 'django.views.generic.simple.direct_to_template', {'template': 'profile.html' }),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
