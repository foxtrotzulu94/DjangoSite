from django.conf.urls import url
from personal_site.views import index, testy
# from django.http.response import HttpResponseForbidden

urlpatterns = [
    url(r'^$', index),
    url(r'^testy/', testy)
    # url(r'^/', HttpResponseForbidden)
]
