from abc import abstractmethod
from django.conf.urls import url

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json


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
                return HttpResponse(data)
        return HttpResponse('<body><p>ObjectNotFound</p></body>')

    @classmethod
    def specific(cls, request, pk):
        """Class method to retrieve a specific model from the DB and return as a JSON object in an HTTP Response"""
        generic_model = cls.main_model()
        if generic_model is not None:
            specific_instance = generic_model.objects.get(pk=pk)
            if specific_instance is not None:
                return HttpResponse(serializers.serialize("json", [specific_instance]))
        return HttpResponse('<body><p>ObjectNotFound</p></body>')

    @classmethod
    def specific_image_list(cls, request, pk):
        """Class method to retrieve a list of URLs that represents a models ImageListField property"""
        generic_model = cls.main_model()
        if generic_model is not None:
            specific_instance = generic_model.objects.get(pk=pk)
            if specific_instance is not None:
                # Try to retrieve the expected ImageListField attribute by name and get an img
                try:
                    model_field = getattr(specific_instance, "display_pictures")
                    field_list = model_field.all()
                    resolved_image_list = []
                    for entry in field_list:
                        resolved_image_list.append(entry.img.url)
                    return HttpResponse(json.dumps(resolved_image_list))

                except AttributeError:
                    print("Queried model has no attributes matching name \"display_pictures\". Request is invalid.")
                    return HttpResponseBadRequest(request)
                # any other exception will cause a very interesting (and probably fatal) exception

        return HttpResponse('<body><p>ObjectNotFound</p></body>')

    @classmethod
    def specific_thumbnail(cls, request, pk):
        """Class method to access the representative thumbnail of a DB model"""
        generic_model = cls.main_model()
        if generic_model is not None:
            specific_instance = generic_model.objects.get(pk=pk)
            if specific_instance is not None:
                # Try to retrieve the expected ImageListField attribute by name and get an img
                try:
                    model_field = getattr(specific_instance, "thumbnail")
                    return HttpResponse(serializers.serialize("json", [model_field.url]))

                except AttributeError:
                    print("Queried model has no attributes matching name \"thumbnail\". Request is invalid.")
                    return HttpResponseBadRequest(request)
                    # any other exception will cause a very interesting (and probably fatal) exception
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
