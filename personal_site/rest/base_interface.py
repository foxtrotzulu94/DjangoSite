from abc import ABCMeta, abstractmethod
from django.conf.urls import include, url

from django.http.response import HttpResponse
from django.core import serializers


class IRest:
    """Base class interface for providing a generic set of operations on models for a REST API. Currently, read-only"""

    @classmethod
    @abstractmethod
    def main_model(cls):
        """Class method used to determine the type being operated on. Subclasses need only override this method"""
        return None

    @classmethod
    def list_all(cls, request):
        """Class method to list all instances of the main_model and return as a JSON object in an HTTP Response"""
        generic_model = cls.main_model()
        if generic_model is not None:
            model_list = generic_model.objects.all()
            if model_list is not None:
                data = serializers.serialize("json", model_list)
                print(data)
                return HttpResponse(data)
        return HttpResponse('<body><p>ObjectNotFound</p></body>')

    @classmethod
    def specific(cls, request, pk):
        """Class method to retrieve a specific model from the DB and return as a JSON object in an HTTP Response"""
        # TODO: Implement
        print(str(request))
        print(str(pk))
        return HttpResponse('<body><p>ObjectNotFound</p></body>')

    @classmethod
    def specific_image_list(cls, request, pk):
        """Class method to retrieve a list of URLs that represents a models ImageListField property"""
        # TODO: Implement
        return HttpResponse('<body><p>ObjectNotFound</p></body>')

    @classmethod
    def specific_thumbnail(cls, request, pk):
        """Class method to access the representative thumbnail of a DB model"""
        # TODO: Implement
        return HttpResponse('<body><p>ObjectNotFound</p></body>')

    @classmethod
    def generate_url(cls):
        """Class method to register subclasses with specific url handlers. Note that the urlpattern list being added to
        must have a unique regex before the include or it will overshadow other url pattern entries
        (e.g.     url(r'^example/projects/', Exmp.generate_url)), where Exmp is a class that inherits from IRest)
        """
        print("Generated urlpatterns mapping for class "+str(cls.__name__))
        return [
            url(r'^$', cls.list_all),
            url(r'^(?P<pk>[0-9]*)$', cls.specific),
            url(r'^(?P<pk>[0-9]*)/images/', cls.specific_image_list),
            url(r'^(?P<pk>[0-9]*)/thumbnail/', cls.specific_thumbnail),
        ]

# end abstract class IRest
