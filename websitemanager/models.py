from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from datetime import datetime
from django.db.models import permalink
from django.http import HttpRequest
from campaignmanager.websitemanager.forms import *

from django.forms import ModelForm

class Account(models.Model):
    name = models.CharField(max_length=150)
    website_title = models.CharField(max_length=200)
    keywords = models.TextField()
    description = models.TextField()
    is_enabled = models.BooleanField(default=True)
    analytics_code = models.TextField(blank=True, null=True)
    email_subscriber_thanks_url = models.CharField(max_length=100, blank=True, null=True)
    footer_content = models.TextField()
    email_subscriber_form = None
    
    def __unicode__(self):
        return self.name
    
    def get_admin_edit_url(self):
        return "/manager/account/edit"
    
    def get_email_subscriber_form(self):
        if self.email_subscriber_form is None:
            #subscriber = EmailSubscriber()
            #subscriber.source = 'website_email_form'
            #subscriber.account = self.account
            self.email_subscriber_form = EmailSubscriberForm()
        return self.email_subscriber_form
    
    def get_email_subscriber_action_url(self):
        return EmailSubscriptionPage.objects.get(account=self).get_absolute_url()
    
    def domains(self):
        return self.domain_set.all()
    
    def users(self):
        return self.accountuser_set.all()
    
    def pages(self):
        return self.page_set.order_by('ordinal')
    
    def primary_pages(self):
        return self.page_set.filter(navigation_area='primary')
    
    def secondary_pages(self):
        return self.page_set.filter(navigation_area='secondary')
    
    def tertiary_pages(self):
        return self.page_set.filter(navigation_area='tertiary')
    
    def GetCurrentAccount(request):
        host = request.get_host()
        print host
        print "!!!!!!!!"
        return Account.objects.get(id=1)
    
    def GetPage(self, current_path):
        print current_path
        return Page.objects.get(account=self, slug=current_path)
    
    def GetHomePage(self):
        return Page.objects.get(account=self, is_home_page=True)
    
    def GetUser(self, current_username):
        return AccountUser.objects.get(account=self, username=current_username)
    
    GetCurrentAccount = staticmethod(GetCurrentAccount)

class AccountUser(User):
    account = models.ForeignKey(Account)
    
    def get_admin_edit_url(self):
        return "/manager/users/" + self.username + "/edit"

NAVIGATION_AREA_OPTIONS = (('primary','Primary Navigation'), ('secondary','Secondary Navigation'), ('tertiary','Tertiary Navigation')) 

class Page(models.Model):
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    keywords = models.TextField()
    account = models.ForeignKey(Account)
    ordinal = models.IntegerField(default=0)
    is_enabled = models.BooleanField(default=True)
    is_home_page = models.BooleanField(default=False)
    navigation_area = models.CharField(max_length=20, choices=NAVIGATION_AREA_OPTIONS, blank=True, null=True)
    parent_page = models.ForeignKey('self', blank=True, null=True)
    type = None
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        if self.is_home_page:
            return "/"
        if self.pagetype() == 'externalpage':
            return self.externalpage.external_url
        return "/" + self.slug
    
    def get_admin_edit_url(self):
        return "/manager/pages/" + self.slug + "/edit"
        
    def Cast(self):
        try:
            page = self.contentpage
            self.type = "contentpage"
        except:
            try:
                page = self.eventpage
                self.type = "eventpage"
            except:
                try:
                    page = self.postpage
                    self.type = "postpage"
                except:
                    try:
                        page = self.externalpage
                        self.type = "externalpage"
                    except:
                        try:
                            page = self.volunteerpage
                            self.type = "volunteerpage"
                        except:
                            try:
                                page = self.emailsubscriptionpage
                                self.type = "emailsubscriptionpage"
                            except:
                                page = self
                                self.type = "page"
        print "Type:" + self.type
        return page
    
    def pagetype(self):
        if self.type == None:
            self.Cast()
        return self.type
    
class ContentPage(Page):
    main_content = models.TextField()
    side_content = models.TextField(blank=True, null=True)
    
class ExternalPage(Page):
    external_url = models.CharField(max_length=200)

class VolunteerPage(Page):
    main_content = models.TextField()
    volunteer_thanks_url = models.CharField(max_length=100, blank=True, null=True)
    form = None;
    
    def get_form(self):
        if self.form == None:
            newvolunteer = Volunteer()
            newvolunteer.account = self.account;
            self.form = VolunteerForm(instance=newvolunteer)
        return self.form
    
class EmailSubscriptionPage(Page):
    main_content = models.TextField()
    email_subscription_thanks_url = models.CharField(max_length=100, blank=True, null=True)
    
EVENT_DISPLAY_OPTIONS = (('list','list'), ('calendar','calendar'))    
    
class EventPage(Page):    
    default_display = models.CharField(max_length=20, choices=EVENT_DISPLAY_OPTIONS, default='list')
    
    def get_admin_events_url(self):
        return "/manager/pages/" + self.slug + "/events"
    
    def get_admin_add_event_url(self):
        return "/manager/pages/" + self.slug + "/events/add"
    
    def events(self):
        return self.event_set.filter(is_published=True).order_by('start_time')
    
    def GetEvent(self, currentslug):
        return self.event_set.filter(slug=currentslug)[0]
    
class Event(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    location_name = models.CharField(max_length=300, blank=True, null=True)
    location_address = models.CharField(max_length=300, blank=True, null=True)
    location_url = models.CharField(max_length=200, blank=True, null=True)
    website_url = models.CharField(max_length=200, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    contact_name = models.CharField(max_length=50, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    page = models.ForeignKey(EventPage)
    is_published = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/" + self.page.slug + "/event/" + self.slug
    
    def get_admin_edit_url(self):
        return "/manager/pages/" + self.page.slug + "/events/" + self.slug + "/edit"

class PostPage(Page):
    posts_per_page = models.IntegerField(default=20)
    
    def get_admin_posts_url(self):
        return "/manager/pages/" + self.slug + "/posts"
    
    def get_admin_add_post_url(self):
        return "/manager/pages/" + self.slug + "/posts/add"
    
    def posts(self):
        return self.post_set.filter(is_published=True).order_by('-published_at')
    
    def GetPost(self, currentslug):
        return self.post_set.filter(slug=currentslug)[0]

class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)
    page = models.ForeignKey(PostPage)

    def __unicode__(self):
        return self.title
    
    def author_name(self):
        return self.author.first_name + " " + self.author.last_name

    def get_absolute_url(self):
        return "/" + self.page.slug + "/post/" + self.slug
    
    def get_admin_edit_url(self):
        return "/manager/pages/" + self.page.slug + "/posts/" + self.slug + "/edit"
    
class Domain(models.Model):
    name = models.CharField(max_length=50)
    account = models.ForeignKey(Account)
    
    def get_admin_edit_url(self):
        return "/manager/domains/" + self.name + "/edit"
    
    def __unicode__(self):
        return self.name
    
class VolunteerOption(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_enabled = models.BooleanField(default=True)
    account = models.ForeignKey(Account)
    
    def __unicode__(self):
        return self.title
    
class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    account = models.ForeignKey(Account)
    selected_options = models.ManyToManyField(VolunteerOption, blank=True, null=True)
    
    def __unicode__(self):
        return self.first_name
    
EMAIL_SUBSCRIPTION_SOURCE_OPTIONS = (('website_volunteer_form','Website Volunteer Form'), ('website_email_form','Website E-mail Form'))
    
class EmailSubscriber(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    source = models.CharField(max_length=20, choices=EMAIL_SUBSCRIPTION_SOURCE_OPTIONS, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    account = models.ForeignKey(Account)
    
    def __unicode__(self):
        return self.email
    
#class Photo(models.Model):
#    title = models.CharField(max_length=50)
#    description = models.CharField(max_length=200)
#    image = models.ImageField(upload_to='photos')
#    account = models.ForeignKey(Account)

from django.forms import MultipleChoiceField, CheckboxSelectMultiple , ModelMultipleChoiceField

class VolunteerForm(ModelForm):
    selected_options = ModelMultipleChoiceField(queryset=VolunteerOption.objects.filter(is_enabled=True), widget=CheckboxSelectMultiple())
    
    class Meta:
        model = Volunteer
        exclude = ('account','is_active',)
    
class EmailSubscriberForm(ModelForm):    
    class Meta:
        model = EmailSubscriber
        fields = ['name', 'email']