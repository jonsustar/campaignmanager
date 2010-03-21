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
    url(r'^admin/', include(admin.site.urls), name='admin_view'),
    
    url(r'^manager/controlpanel', 'campaignmanager.websitemanager.manager.views.controlpanel', name='controlpanel_view'),
    #(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^manager/login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login_view'),
    
    url(r'^manager/logout', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout_view'),
    #url(r'^admin/logout', 'campaignmanager.websitemanager.manager.views.logout', name='logout_view'),
    url(r'^manager/account/edit', 'campaignmanager.websitemanager.manager.views.accountedit', name='accountedit_view'),
    #url(r'^admin/domains/(?P<domain>[-\w]+)/edit$', 'campaignmanager.websitemanager.manager.views.domainedit', name='domainedit_view'),
    #url(r'^admin/domains/add', 'campaignmanager.websitemanager.manager.views.domainadd', name='domainadd_view'),
    url(r'^manager/users/(?P<username>[-\w]+)/edit$', 'campaignmanager.websitemanager.manager.views.useredit', name='useredit_view'),
    url(r'^manager/users/add', 'campaignmanager.websitemanager.manager.views.useradd', name='useradd_view'),
    url(r'^manager/pages/(?P<pageslug>[-\w]+)/edit$', 'campaignmanager.websitemanager.manager.views.pageedit', name='pagedit_view'),
    url(r'^manager/pages/add', 'campaignmanager.websitemanager.manager.views.pageadd', name='pageadd_view'),
    url(r'^manager/pages/(?P<pageslug>[-\w]+)/posts/(?P<postslug>[-\w]+)/edit$', 'campaignmanager.websitemanager.manager.views.postedit', name='postedit_view'),
    url(r'^manager/pages/(?P<pageslug>[-\w]+)/posts/add', 'campaignmanager.websitemanager.manager.views.postadd', name='postadd_view'),
    
    url(r'^manager/pages/(?P<pageslug>[-\w]+)/posts', 'campaignmanager.websitemanager.manager.views.posts', name='posts_view'),
    url(r'^manager/pages/(?P<pageslug>[-\w]+)/events/(?P<eventslug>[-\w]+)/edit$', 'campaignmanager.websitemanager.manager.views.eventedit', name='eventedit_view'),
    url(r'^manager/pages/(?P<pageslug>[-\w]+)/events/add', 'campaignmanager.websitemanager.manager.views.eventadd', name='eventadd_view'),
    url(r'^manager/pages/(?P<pageslug>[-\w]+)/events', 'campaignmanager.websitemanager.manager.views.events', name='events_view'),
    
    #url(r'^admin/', 'campaignmanager.websitemanager.views.mainadmin', name='mainadmin_view'),
    url(r'^(?P<path>[-\w]+)/event/(?P<slug>[-\w]+)$', 'campaignmanager.websitemanager.views.event', name='post_view'),
    url(r'^(?P<path>[-\w]+)/post/(?P<slug>[-\w]+)$', 'campaignmanager.websitemanager.views.post', name='post_view'),
    #url(r'^(?P<path>[-\w]+)/thanks$', 'campaignmanager.websitemanager.views.volunteersubmit', name='volunteersubmit'),
    url(r'^(?P<path>[-\w]+)$', 'campaignmanager.websitemanager.views.page', name='page_view'),
    #(r'^conversations','twibbots.views.conversations')
)
