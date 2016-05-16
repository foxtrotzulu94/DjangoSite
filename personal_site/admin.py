from django.contrib import admin
from personal_site.models import *

# Register your models here.
# Example Models
admin.site.register(ExampleItem)
admin.site.register(ImageListField)


# Actual Models that are displayed throughout the site
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'external_link')
# end class


@admin.register(WorkExperience, ExtracurricularExperience, VolunteerExperience)
class ExperienceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'location', 'start_date', 'end_date', 'ongoing')
# end class


@admin.register(PersonalProject, GameTitle, PersonalInterest)
class GeneralDisplayItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'ongoing')
# end class
