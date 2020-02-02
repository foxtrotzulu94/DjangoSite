from django.contrib import admin
from django.utils.safestring import mark_safe
from personal_site.models import *

# Register your models here.
# Example Models
admin.site.register(ExampleItem)


# Actual Models that are displayed throughout the site
@admin.register(ContactInfo, GameTitle)
class SimpleInfoAdmin(admin.ModelAdmin):
    def preview_thumbnail(self, model):
        if model.thumbnail.name is not "":
            return mark_safe('<img src="%s" width="auto" height="64"/>' % model.thumbnail.url)
        else:
            return u'No Thumbnail available'
    preview_thumbnail.allow_tags = True

    list_display = ('preview_thumbnail', 'title', 'external_link')
# end class


@admin.register(WorkExperience, ExtracurricularExperience, VolunteerExperience)
class ExperienceItemAdmin(admin.ModelAdmin):
    def preview_thumbnail(self, model):
        if model.thumbnail.name is not "":
            return mark_safe('<img src="%s" width="auto" height="64"/>' % model.thumbnail.url)
        else:
            return u'No Thumbnail available'
    preview_thumbnail.allow_tags = True

    list_display = ('preview_thumbnail', 'title', 'organization', 'location', 'start_date', 'end_date', 'ongoing')
# end class


@admin.register(PersonalProject)
class GeneralDisplayItemAdmin(admin.ModelAdmin):
    def preview_thumbnail(self, model):
        type(model.thumbnail)
        if model.thumbnail.name is not "":
            return mark_safe('<img src="%s" width="auto" height="64"/>' % model.thumbnail.url)
        else:
            return u'No Thumbnail available'
    preview_thumbnail.allow_tags = True

    list_display = ('preview_thumbnail', 'title', 'start_date', 'end_date', 'ongoing')
# end class


@admin.register(Award)
class AwardHonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'entity', 'location', 'date')
# end class
