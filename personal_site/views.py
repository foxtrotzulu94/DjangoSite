from django.shortcuts import render
from django.core import serializers
from django.views.decorators.cache import never_cache
# Create your views here.

from django.views.decorators.http import require_safe
from django.http.response import HttpResponse
from .models import ExampleItem


@require_safe
def index(request):
    """Display the initial website"""
    return render(
        request,
        'index.html'
    )

@never_cache
def testy(request):
    return render(
        request,
        'testy.html'
    )


def ajaj(request):
    retVal = ExampleItem.objects.get(pk=1)
    if retVal is not None:
        data = serializers.serialize("json", [retVal])
        print(data)
        return HttpResponse(data)
    return HttpResponse('<body><p>ObjectNotFound</p></body>')


def list_projects(request):
    # TODO: All projects should be ordered by Date
    retVal = ExampleItem.objects.all()
    if retVal is not None:
        data = serializers.serialize("json", retVal)
        print(data)
        return HttpResponse(data)
    return HttpResponse('<body><p>ObjectNotFound</p></body>')

