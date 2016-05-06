from django.conf.urls import url
from personal_site.views import *

from django.conf import settings
from django.conf.urls.static import static
# from django.http.response import HttpResponseForbidden

urlpatterns = [
    url(r'^$', index),
    url(r'^testy/', testy),
    url(r'^ajaj', ajaj),
    # url(r'^/', HttpResponseForbidden)
    url(r'^data/projects', list_projects),
    # url(r'^data/projects/?P<deptnum>[A-z]{4}[0-9]{3}',), # TODO: fill this in
    # url(r'^data/games'),
    # url(r'^data/interests')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
