from django.contrib import admin
from personal_site.models import *

# Register your models here.
# Example Models
# admin.site.register(ImageListField)


# Actual Models that are displayed throughout the site
@admin.register(ImageListField)
class ImagePoolAdmin(admin.ModelAdmin):
    def show_image(self, model):
        return u'<img src=\"%s\" width=\"auto\" height=\"100\"/>' % str(model.img.url)
    show_image.allow_tags = True

    list_display = ('show_image', '__str__')
# end class


@admin.register(ContactInfo, GameTitle)
class SimpleInfoAdmin(admin.ModelAdmin):
    def preview_thumbnail(self, model):
        if model.thumbnail.name is not "":
            return u'<img src=\"%s\" width=\"auto\" height=\"64\"/>' % str(model.thumbnail.url)
        else:
            return u'No Thumbnail available'
    preview_thumbnail.allow_tags = True

    list_display = ('preview_thumbnail', 'title', 'external_link')
# end class


@admin.register(WorkExperience, ExtracurricularExperience, VolunteerExperience)
class ExperienceItemAdmin(admin.ModelAdmin):
    def preview_thumbnail(self, model):
        if model.thumbnail.name is not "":
            return u'<img src=\"%s\" width=\"auto\" height=\"64\"/>' % str(model.thumbnail.url)
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
            return u'<img src=\"%s\" width=\"auto\" height=\"64\"/>' % str(model.thumbnail.url)
        else:
            return u'No Thumbnail available'
    preview_thumbnail.allow_tags = True

    list_display = ('preview_thumbnail', 'title', 'start_date', 'end_date', 'ongoing')
# end class


@admin.register(Award)
class AwardHonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'entity', 'location', 'date')
# end class
