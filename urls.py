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
    #url(r'^administrator/post', 'campaignmanager.websitemanager.views.postadmin', name='postadmin_view'),
    url(r'^master/', include(admin.site.urls), name='admin_view'),
    #url(r'^admin/controlpanel', 'campaignmanager.websitemanager.admin.views.controlpanel', name='controlpanel_view'),
    
    #url(r'^admin/login', 'campaignmanager.websitemanager.admin.views.login', name='login_view'),
    #url(r'^admin/logout', 'campaignmanager.websitemanager.admin.views.logout', name='logout_view'),
    #url(r'^admin/account/edit', 'campaignmanager.websitemanager.admin.views.accountedit', name='accountedit_view'),
    #url(r'^admin/domains/(?P<domain>[-\w]+)/edit$', 'campaignmanager.websitemanager.admin.views.domainedit', name='domainedit_view'),
    #url(r'^admin/domains/add', 'campaignmanager.websitemanager.admin.views.domainadd', name='domainadd_view'),
    #url(r'^admin/users/(?P<username>[-\w]+)/edit$', 'campaignmanager.websitemanager.admin.views.useredit', name='useredit_view'),
    #url(r'^admin/users/add', 'campaignmanager.websitemanager.admin.views.useradd', name='useradd_view'),
    #url(r'^admin/pages/(?P<pageslug>[-\w]+)/edit$', 'campaignmanager.websitemanager.admin.views.pageedit', name='pagedit_view'),
    #url(r'^admin/pages/add', 'campaignmanager.websitemanager.admin.views.pageadd', name='pageadd_view'),
    #url(r'^admin/pages/(?P<pageslug>[-\w]+)/posts/(?P<postslug>[-\w]+)/edit$', 'campaignmanager.websitemanager.admin.views.postedit', name='postedit_view'),
    #url(r'^admin/pages/(?P<pageslug>[-\w]+)/posts/add', 'campaignmanager.websitemanager.admin.views.postadd', name='postadd_view'),
    #url(r'^admin/pages/(?P<pageslug>[-\w]+)/events/(?P<eventslug>[-\w]+)/edit$', 'campaignmanager.websitemanager.admin.views.eventedit', name='eventedit_view'),
    #url(r'^admin/pages/(?P<pageslug>[-\w]+)/events/add', 'campaignmanager.websitemanager.admin.views.eventadd', name='eventadd_view'),

    url(r'^admin/account/edit', 'campaignmanager.websitemanager.views.accountadmin', name='accountadmin_view'),
    url(r'^admin/page/(?P<path>[-\w]+)/edit$', 'campaignmanager.websitemanager.views.pageadmin', name='pageadmin_view'),
    url(r'^admin/', 'campaignmanager.websitemanager.views.mainadmin', name='mainadmin_view'),
    url(r'^(?P<path>[-\w]+)/post/(?P<slug>[-\w]+)$', 'campaignmanager.websitemanager.views.post', name='post_view'),
    url(r'^(?P<path>[-\w]+)$', 'campaignmanager.websitemanager.views.page', name='page_view'),
    url(r'^', 'campaignmanager.websitemanager.views.home', name='home_view'),
    #(r'^conversations','twibbots.views.conversations')
)
