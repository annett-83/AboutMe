from django.contrib import admin
from django.urls import path, include
from .views import default_view, myhobby_view, aboutme_view, contact_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', default_view, name='default'),
    path('myhobby/', myhobby_view, name='myhobby'),
    path('aboutme/', aboutme_view, name='aboutme'),
    path('contact/', contact_view, name='contact'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)