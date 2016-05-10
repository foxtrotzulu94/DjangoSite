from django.contrib import admin
from personal_site.models import *

# Register your models here.

# Example Models
admin.site.register(ExampleItem)
admin.site.register(ImageListField)
# admin.site.register(DisplayItem)
# admin.site.register(ExperienceItem)

# Actual Models that are displayed throughout the site
admin.site.register(WorkExperience)
admin.site.register(VolunteerExperience)
admin.site.register(ExtracurricularExperience)
admin.site.register(PersonalProject)
admin.site.register(GameTitle)
admin.site.register(PersonalInterest)

