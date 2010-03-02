from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from datetime import datetime
from django.db.models import permalink
from django.http import HttpRequest

class Account(models.Model):
    name = models.CharField(max_length=300)
    
    def __unicode__(self):
        return self.name
    
    def GetCurrentAccount(request):
        host = request.get_host()
        print host
        print "!!!!!!!!"
        return Account.objects.get(id=1)
    
    def GetPage(self, current_path):
        return Page.objects.get(account=self, path=current_path)
    
    GetCurrentAccount = staticmethod(GetCurrentAccount)

class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    account = models.ForeignKey(Account)
    
    def __unicode__(self):
        return self.title
    
class ContentPage(Page):
    main_content = models.TextField()
    side_content = models.TextField()
    
EVENT_DISPLAY_OPTIONS = (('list','list'), ('calendar','calendar'))    
    
class EventPage(Page):    
    default_display = models.CharField(max_length=20, choices=EVENT_DISPLAY_OPTIONS, default='list')
    
class Event(models.Model):
    name = models.CharField(max_length=300)
    page = models.ForeignKey(EventPage)
    
    def __unicode__(self):
        return self.name

class PostPage(Page):
    posts_per_page = models.IntegerField()

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published_at = models.DateTimeField(default=datetime.now)
    page = models.ForeignKey(PostPage)

    def __unicode__(self):
        return self.title
    
    def author_name(self):
        return self.author.first_name + " " + self.author.last_name
    
    @models.permalink
    def get_absolute_url(self):
        return ('post_view', [self.slug])
    
class Domain(models.Model):
    name = models.CharField(max_length=50)
    account = models.ForeignKey(Account)
    
    def __unicode__(self):
        return self.name
    
