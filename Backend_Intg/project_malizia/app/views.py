from django.shortcuts import render
from app.models import *


def index(request):
    section_5s = Section_5.objects.all()
    testimonials = Section8.objects.all()
    return render(request, 'index.html', {
        'section_5s': section_5s,
        'testimonials': testimonials
    })

def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def projects(request):
    return render(request, 'projects.html')


def clients(request):
    return render(request, 'clients.html')


def blogs(request):
    return render(request, 'blogs.html')


def careers(request):
    return render(request, 'careers.html')


def contact(request):
    return render(request, 'contact.html')
