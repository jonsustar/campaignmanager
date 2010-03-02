from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^twibbots/', include('twibbots_django.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': (settings.STATIC_DOC_ROOT + '/js')}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': (settings.STATIC_DOC_ROOT + '/css')}),
    (r'^img/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': (settings.STATIC_DOC_ROOT + '/img')}),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls), name='admin_view'),
    url(r'^(?P<path>[-\w]+)$', 'campaignmanager.websitemanager.views.page', name='page_view'),
    url(r'^', 'campaignmanager.websitemanager.views.home', name='home_view'),
    #(r'^conversations','twibbots.views.conversations')
)
