from django.shortcuts import render
from django.core import serializers
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_safe
from django.http.response import HttpResponse
from personal_site.models import WorkExperience


def list_all(request):
    pass


def specific(request, pk):
    pass


def specific_image_list(request, pk):
    pass


def specific_thumbnail(request, pk):
    pass

