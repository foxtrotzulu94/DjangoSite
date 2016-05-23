from django.conf.urls import include, url
from django.views.generic.base import View

# This URL file includes all the URLs that map to functions in this directory

# Imports for REST API implementation
from .implementation import SerializedExtracurricularExperience, SerializedGameTitles, SerializedInterests, \
    SerializedProjects, SerializedVolunteerExperience, SerializedWorkExperience

# 'Experience' REST API URLs
urlpatterns = [
    # url(r'^data/$', View("nothing")),
    url(r'^data/work_exp/', include(SerializedWorkExperience.generate_url())),
    url(r'^data/extra_exp/', include(SerializedExtracurricularExperience.generate_url())),
    url(r'^data/volunteer/', include(SerializedVolunteerExperience.generate_url())),
    url(r'^data/projects/', include(SerializedProjects.generate_url())),
    url(r'^data/titles/', include(SerializedGameTitles.generate_url())),
    url(r'^data/interests/', include(SerializedInterests.generate_url()))
]
