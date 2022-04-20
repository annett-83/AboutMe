from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
from django.shortcuts import redirect

def default_view(request):
    return render(request, 'flatpages/ich.html', {
    })

def aboutme_view(request):
    return render(request, 'flatpages/aboutme.html', {
    })

def myhobby_view(request):
    return render(request, 'flatpages/myhobby.html', {
    })

def contact_view(request):
    return render(request, 'flatpages/contact.html', {
    })
