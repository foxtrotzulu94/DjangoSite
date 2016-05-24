from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from personal_site.views import *

urlpatterns = [
    url(r'^$', index),

    url(r'', include('personal_site.rest.urls')),

    # ImageListField Query
    url(r'^images/(?P<img>[0-9]*)$', image_field_retrieval),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
