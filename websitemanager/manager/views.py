from campaignmanager.websitemanager.models import *
from campaignmanager.websitemanager.manager.forms import *
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required

AFTER_POST_REDIRECT_URL = '/manager/controlpanel'

#@login_required
def controlpanel(request):
    currentaccount = Account.GetCurrentAccount(request)

    templatefile = 'controlpanel.html'
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount
    })
    return HttpResponse(t.render(c))

def accountedit(request):
    currentaccount = Account.GetCurrentAccount(request)

    if request.method == 'POST': # If the form has been submitted...
        form = AccountForm(request.POST, instance=currentaccount) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect(AFTER_POST_REDIRECT_URL) # Redirect after POST
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

def useradd(request):
    currentaccount = Account.GetCurrentAccount(request)
    currentuser = AccountUser()
    currentuser.account = currentaccount
    form = None
    
    templatefile = 'useredit.html'
    
    if request.method == 'POST': # If the form has been submitted...
        form = AccountUserForm(request.POST, instance=currentuser) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect(AFTER_POST_REDIRECT_URL) # Redirect after POST
    else:
        form = AccountUserForm(instance=currentuser) # An unbound form
        
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentuser' : currentuser,
        'form' : form
    })
    return HttpResponse(t.render(c)) 

def useredit(request, username):
    currentaccount = Account.GetCurrentAccount(request)
    currentuser = currentaccount.GetUser(username)
    form = None
    
    templatefile = 'useredit.html'
    
    if request.method == 'POST': # If the form has been submitted...
        form = AccountUserForm(request.POST, instance=currentuser) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect(AFTER_POST_REDIRECT_URL) # Redirect after POST
    else:
        form = AccountUserForm(instance=currentuser) # An unbound form
        
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentuser' : currentuser,
        'form' : form
    })
    return HttpResponse(t.render(c)) 

def pageadd(request):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = Page()
    currentpage.account = currentaccount
    pagetype = request.REQUEST["pagetype"]
    form = None
    
    print 'PAGETYPE!!!:' + pagetype
    
    if pagetype == "contentpage":
        templatefile = 'contentpageedit.html'
        print 'here'
        if request.method == 'POST': # If the form has been submitted...
            form = ContentPageForm(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                form.save()
                return HttpResponseRedirect(AFTER_POST_REDIRECT_URL) # Redirect after POST
        else:
            form = ContentPageForm(instance=currentpage) # An unbound form
        
    else:
        if pagetype == 'postpage':
            templatefile = 'postpageedit.html'
            
            if request.method == 'POST':
                form = PostPageForm(request.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(AFTER_POST_REDIRECT_URL)
            else:
                form = PostPageForm(instance=currentpage)
   
        else:    
            if pagetype == 'eventpage':
                templatefile = 'eventpageedit.html'
                
                if request.method == 'POST':
                    form = EventPageForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return HttpResponseRedirect(AFTER_POST_REDIRECT_URL)
                else:
                    form = EventPageForm(instance=currentpage)
            else:
                if pagetype == 'externalpage':
                    templatefile = 'externalpageedit.html'
                    
                    if request.method == 'POST':
                        form = ExternalPageForm(request.POST)
                        if form.is_valid():
                            form.save()
                            return HttpResponseRedirect(AFTER_POST_REDIRECT_URL)
                    else:
                        form = ExternalPageForm(instance=currentpage)
                
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentpage' : currentpage,
        'form' : form
    })
    return HttpResponse(t.render(c))  

def pageedit(request, pageslug):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = currentaccount.GetPage(pageslug).Cast()
    form = None
    
    if type(currentpage) == type(ContentPage()):
        templatefile = 'contentpageedit.html'
        
        if request.method == 'POST': # If the form has been submitted...
            form = ContentPageForm(request.POST, instance=currentpage) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                form.save()
                return HttpResponseRedirect(AFTER_POST_REDIRECT_URL) # Redirect after POST
        else:
            form = ContentPageForm(instance=currentpage) # An unbound form
        
    else:
        if type(currentpage) == type(PostPage()):
            templatefile = 'postpageedit.html'
            
            if request.method == 'POST':
                form = PostPageForm(request.POST, instance=currentpage)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(AFTER_POST_REDIRECT_URL)
            else:
                form = PostPageForm(instance=currentpage)
   
        else:    
            if type(currentpage) == type(EventPage()):
                templatefile = 'eventpageedit.html'
                
                if request.method == 'POST':
                    form = EventPageForm(request.POST, instance=currentpage)
                    if form.is_valid():
                        form.save()
                        return HttpResponseRedirect(AFTER_POST_REDIRECT_URL)
                else:
                    form = EventPageForm(instance=currentpage)
            else:
                if type(currentpage) == type(ExternalPage()):
                    templatefile = 'externalpageedit.html'
                    
                    if request.method == 'POST':
                        form = ExternalPageForm(request.POST, instance=currentpage)
                        if form.is_valid():
                            form.save()
                            return HttpResponseRedirect(AFTER_POST_REDIRECT_URL)
                    else:
                        form = ExternalPageForm(instance=currentpage)
                
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentpage' : currentpage,
        'form' : form
    })
    return HttpResponse(t.render(c))  

def posts(request, pageslug):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = currentaccount.GetPage(pageslug).Cast()
    
    templatefile = 'posts.html'

    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentpage' : currentpage,
    })
    return HttpResponse(t.render(c))  

def postedit(request, pageslug, postslug):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = currentaccount.GetPage(pageslug).Cast()
    currentpost = currentpage.GetPost(postslug)
    form = None
    
   
    templatefile = 'postedit.html'
    
    if request.method == 'POST': # If the form has been submitted...
        form = PostForm(request.POST, instance=currentpost) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect(AFTER_POST_REDIRECT_URL) # Redirect after POST
    else:
        form = PostForm(instance=currentpost) # An unbound form
                
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentpage' : currentpage,
        'currentpost' : currentpost,
        'form' : form
    })
    return HttpResponse(t.render(c))  

def postadd(request, pageslug):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = currentaccount.GetPage(pageslug).Cast()
    currentpost = Post()
    currentpost.page = currentpage
    form = None
    
   
    templatefile = 'postedit.html'
    
    if request.method == 'POST': # If the form has been submitted...
        form = PostForm(request.POST, instance=currentpost) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect(AFTER_POST_REDIRECT_URL) # Redirect after POST
    else:
        form = PostForm(instance=currentpost) # An unbound form
                
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentpage' : currentpage,
        'currentpost' : currentpost,
        'form' : form
    })
    return HttpResponse(t.render(c))  

def events(request, pageslug):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = currentaccount.GetPage(pageslug).Cast()
    
    templatefile = 'events.html'

    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentpage' : currentpage,
    })
    return HttpResponse(t.render(c)) 

def eventedit(request, pageslug, eventslug):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = currentaccount.GetPage(pageslug).Cast()
    currentevent = currentpage.GetEvent(eventslug)
    form = None
    
   
    templatefile = 'eventedit.html'
    
    if request.method == 'POST': # If the form has been submitted...
        form = EventForm(request.POST, instance=currentevent) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect(AFTER_POST_REDIRECT_URL) # Redirect after POST
    else:
        form = EventForm(instance=currentevent) # An unbound form
                
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentpage' : currentpage,
        'currentevent' : currentevent,
        'form' : form
    })
    return HttpResponse(t.render(c))  

def eventadd(request, pageslug):
    currentaccount = Account.GetCurrentAccount(request)
    currentpage = currentaccount.GetPage(pageslug).Cast()
    currentevent = Event()
    currentevent.page = currentpage
    form = None
    
   
    templatefile = 'eventedit.html'
    
    if request.method == 'POST': # If the form has been submitted...
        form = EventForm(request.POST, instance=currentevent) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect(AFTER_POST_REDIRECT_URL) # Redirect after POST
    else:
        form = EventForm(instance=currentevent) # An unbound form
                
    t = loader.get_template(templatefile)
    c = None
    c = Context({
        'currentaccount' : currentaccount,
        'currentpage' : currentpage,
        'currentevent' : currentevent,
        'form' : form
    })
    return HttpResponse(t.render(c))  