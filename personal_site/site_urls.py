from django.conf.urls import url
from personal_site.views import index, testy, ajaj

from django.conf import settings
from django.conf.urls.static import static
# from django.http.response import HttpResponseForbidden

urlpatterns = [
    url(r'^$', index),
    url(r'^testy/', testy),
    url(r'^ajaj', ajaj)
    # url(r'^/', HttpResponseForbidden)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
