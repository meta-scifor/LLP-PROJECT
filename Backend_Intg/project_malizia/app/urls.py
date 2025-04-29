from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('projects', projects, name='projects'),
    path('clients', clients, name='clients'),
    path('blogs', blogs, name='blogs'),
    path('careers', careers, name='careers'),
    path('contact', contact, name='contact'),
]