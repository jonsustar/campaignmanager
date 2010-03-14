from campaignmanager.websitemanager.models import *
from django.db import models
from django.forms import ModelForm

class AccountForm(ModelForm):
    class Meta:
        model = Account
        
class ContentPageForm(ModelForm):
    class Meta:
        model = ContentPage
        
class PostPageForm(ModelForm):
    class Meta:
        model = PostPage
        
class Post(ModelForm):
    class Meta:
        model = Post
        
class Domain(ModelForm):
    class Meta:
        model = Domain