from campaignmanager.websitemanager.models import *
from campaignmanager.websitemanager.forms import *
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

def home(request):
    account = Account.GetCurrentAccount(request)
    
    t = loader.get_template('base.html')
    c = None
    c = Context({
        'posts' : None, 
        'active_bots' : None,
        'breadcrumbs' : None,
        'title' : account.name
    })
    return HttpResponse(t.render(c))

def page(request, path):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = currentaccount.GetPage(path).Cast()
    #allpages = account.pages
    
    templatefile = 'base.html'
    
    if type(currentpage) == type(ContentPage()):
        templatefile = 'contentpage.html'
    else:
        if type(currentpage) == type(PostPage()):
            templatefile = 'postpage.html'
        else:    
            if type(currentpage) == type(EventPage()):
                templatefile = 'eventpage.html'
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentpage' : currentpage,
        'currentaccount' : currentaccount
    })
    return HttpResponse(t.render(c))

def post(request, path, slug):
    currentaccount = Account.GetCurrentAccount(request)
    print currentaccount
    currentpage = currentaccount.GetPage(path).Cast()
    print currentpage
    currentpost = currentpage.GetPost(slug)
    print currentpost
    #allpages = account.pages
    
    templatefile = 'post.html'
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentpage' : currentpage,
        'currentaccount' : currentaccount,
        'currentpost' : currentpost
    })
    return HttpResponse(t.render(c))

def mainadmin(request):
    currentaccount = Account.GetCurrentAccount(request)

    templatefile = 'mainadmin.html'
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount
    })
    return HttpResponse(t.render(c))

def accountadmin(request):
    currentaccount = Account.GetCurrentAccount(request)

    if request.method == 'POST': # If the form has been submitted...
        form = AccountForm(request.POST, instance=currentaccount) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/admin/') # Redirect after POST
    else:
        form = AccountForm(instance=currentaccount) # An unbound form



    templatefile = 'accountadmin.html'
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'form' : form
    })
    return HttpResponse(t.render(c))

def pageadmin(request, path):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = currentaccount.GetPage(path).Cast()
    form = None
    
    if type(currentpage) == type(ContentPage()):
        templatefile = 'contentpageadmin.html'
        
        if request.method == 'POST': # If the form has been submitted...
            form = ContentPageForm(request.POST, instance=currentpage) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                form.save()
                return HttpResponseRedirect('/admin/') # Redirect after POST
        else:
            form = ContentPageForm(instance=currentpage) # An unbound form
        
    else:
        if type(currentpage) == type(PostPage()):
            templatefile = 'postpage.html'
        else:    
            if type(currentpage) == type(EventPage()):
                templatefile = 'eventpage.html'
                
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentpage' : currentpage,
        'form' : form
    })
    return HttpResponse(t.render(c))  

from django import forms

class PostForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


def postadmin(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/postsubmitted')
    else:
        form = PostForm()
        
    t = loader.get_template('base_admin.html')
    c = None
    c = Context({
            'form' : form
    })
    return HttpResponse(t.render(c))