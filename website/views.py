from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages



def index_view(request):
    return render(request, 'website/index.html')

def latest_view(request):
    return render(request, 'website/latest-posts.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submit successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submitted!!!')
    form = ContactForm()   
    return render(request, 'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')






def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():#
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = ContactForm()
    return render(request, 'test.html',{'form':form})





