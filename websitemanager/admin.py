from campaignmanager.websitemanager.models import *
from django.contrib.sites.models import Site
from django.contrib import admin
from django import forms
#from tinymce.widgets import TinyMCE

admin.site.register(Post)
admin.site.register(PostPage)
admin.site.register(Event)
admin.site.register(EventPage)
admin.site.register(ContentPage)
admin.site.register(Domain)
admin.site.register(Account)
admin.site.register(Page)