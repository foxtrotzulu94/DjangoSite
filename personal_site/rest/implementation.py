from django.conf.urls import include, url

from personal_site.models import WorkExperience, ExtracurricularExperience, VolunteerExperience
from personal_site.models import PersonalProject, GameTitle
from personal_site.models import PersonalInterest

from .base_interface import IRest


class SerializedWorkExperience(IRest):
    @classmethod
    def main_model(cls):
        return WorkExperience
# end class SerialWorkExp


class SerializedExtracurricularExperience(IRest):
    @classmethod
    def main_model(cls):
        return ExtracurricularExperience
# end class SerialExtraExp


class SerializedVolunteerExperience(IRest):
    @classmethod
    def main_model(cls):
        return VolunteerExperience
# end class SerialWorkExp


class SerializedProjects(IRest):
    @classmethod
    def main_model(cls):
        return PersonalProject
# end class SerialWorkExp


class SerializedGameTitles(IRest):
    @classmethod
    def main_model(cls):
        return WorkExperience
# end class SerialWorkExp


class SerializedInterests(IRest):
    @classmethod
    def main_model(cls):
        return WorkExperience
# end class SerialWorkExp


