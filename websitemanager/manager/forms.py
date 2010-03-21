from campaignmanager.websitemanager.models import *
from django.db import models
from django.forms import ModelForm
from django.forms import CharField
from tinymce.widgets import TinyMCE

class AccountForm(ModelForm):
    class Meta:
        model = Account
 
class AccountUserForm(ModelForm):
    class Meta:
        model = AccountUser
        
class ContentPageForm(ModelForm):
    main_content = CharField(widget=TinyMCE(attrs={'cols': 55, 'rows': 15},))
    side_content = CharField(widget=TinyMCE(attrs={'cols': 55, 'rows': 15},))
    class Meta:
        model = ContentPage

class ExternalPageForm(ModelForm):
    class Meta:
        model = ExternalPage

class EventPageForm(ModelForm):
    class Meta:
        model = EventPage

class EventForm(ModelForm):
    class Meta:
        model = Event
        
class PostPageForm(ModelForm):
    class Meta:
        model = PostPage
        
class PostForm(ModelForm):
    content = CharField(widget=TinyMCE(attrs={'cols': 55, 'rows': 15},))
    
    class Meta:
        model = Post
        
class DomainForm(ModelForm):
    class Meta:
        model = Domain
        
