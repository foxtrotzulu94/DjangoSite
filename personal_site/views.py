from django.shortcuts import render
from django.core import serializers
from django.views.decorators.cache import never_cache
# Create your views here.

from django.views.decorators.http import require_safe
from django.http.response import HttpResponse
from personal_site.models import *

# This file returns an http response that maps to a template.
# For responses linked to pure JSON data, check personal_site.rest folder


@require_safe
def index(request):
    """Display the initial website"""
    work_items = WorkExperience.objects.all().order_by('-end_date')
    extracurricular_items = ExtracurricularExperience.objects.all().order_by('-end_date')
    volunteer_items = VolunteerExperience.objects.all().order_by('-end_date')
    contact = ContactInfo.objects.all()
    projects = PersonalProject.objects.all()
    print(projects)
    games = GameTitle.objects.all()
    return render(
        request,
        'index.html',
        {'work': work_items,
         'extracurricular': extracurricular_items,
         'volunteer': volunteer_items,
         'projects': projects,
         'games': games,
         'contact_info': contact
         }
    )


def image_field_retrieval(request, img):
    pass

