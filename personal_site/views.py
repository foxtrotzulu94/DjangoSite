from django.shortcuts import render

# Create your views here.

from django.views.decorators.http import require_safe
from django.template import loader


@require_safe
def index(request):
    """Display the initial website"""
    return render(
        request,
        'index.html'
    )


def testy(request):
    return render(
        request,
        'testy.html'
    )

