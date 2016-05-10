from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from personal_site.views import *

urlpatterns = [
    url(r'^$', index),

    # Testing URLs, comment out for release
    url(r'^testy/', testy),
    url(r'^ajaj/', ajaj),

    url(r'', include('personal_site.rest.urls')),
    url(r'^example/projects/', list_projects),

    # ImageListField Query
    url(r'^images/?P<img>[0-9]*$', image_field_retrieval),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
