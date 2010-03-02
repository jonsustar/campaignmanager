from campaignmanager.websitemanager.models import *
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

def home(request):
    account = Account.GetCurrentAccount(request)
    
    t = loader.get_template('blog.html')
    c = None
    c = Context({
        'posts' : None, 
        'active_bots' : None,
        'breadcrumbs' : None,
        'title' : account.name
    })
    return HttpResponse(t.render(c))

def page(request, path):
    account = Account.GetCurrentAccount(request)
    page = account.GetPage(path)
    
    t = loader.get_template('base.html')
    c = None
    c = Context({
        'page' : page
    })
    return HttpResponse(t.render(c))  