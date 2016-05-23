from django.db import models
from datetime import date

# TODO: Break up this file AND add the following models: "Honors", "Awards", "Publications", "Presentations"


class ImageListField(models.Model):
    """Class for linking a Model to a list of Images"""
    img = models.ImageField(upload_to='media/')

    def preview(self):
        return u'<img src=\"%s\" />' % str(self.img.url)

    def __str__(self):
        return self.img.name+" - ("+str(self.img.width)+"x"+str(self.img.height)+")"
# end class ImageModel


class ExampleItem(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    img = models.ImageField(upload_to='media/', blank=True)  # TODO: Remove in production server
    start_date = models.DateField(default=date.today)

    list_images = models.ManyToManyField(ImageListField, blank=True)

    def __str__(self):
        return self.title
# end class


class DisplayItem(models.Model):
    """Abstract Class representing a generic, displayable element"""

    title = models.CharField(max_length=30)
    thumbnail = models.ImageField(upload_to='media/', blank=True)  # TODO: Remove in production server

    class Meta:
        abstract = True
# end class DisplayItem


class DetailedDisplayItem(DisplayItem):
    """Abstract Class used to model/define Experience items"""

    highlights = models.CharField(max_length=200, blank=True, help_text="Tech used, skills learnt or lessons learnt")
    description = models.TextField(help_text="Short and sweet summary of the experience. Use Bullet Point sentences!")
    display_pictures = models.ManyToManyField(ImageListField,  blank=True, help_text="Relevant images")

    # These are displayed differently on the View depending on which subclass they are
    start_date = models.DateField(default=date.today)
    ongoing = models.BooleanField(default=False, help_text="Is this still current and ongoing?")
    end_date = models.DateField(default=date.today, help_text="Only displayed if Ongoing is false")

    def __str__(self):
        return self.title+" ("+self.start_date.strftime("%B %Y")+"-"+self.start_date.strftime("%B %Y")+")"

    class Meta:
        abstract = True
# end class

""" ### Section 2 Models ### """


class ExperienceItem(DetailedDisplayItem):
    """Generic Class for all Section 2 Items"""
    # title corresponds to Position in this case
    organization = models.CharField(max_length=50, help_text="Company, Society, Group")
    location = models.CharField(max_length=50)
    # URL to the external site
    ext_url = models.URLField(blank=True, help_text="Link to more information")

    def __str__(self):
        return self.title + " at " + self.organization + " (" + self.location + " | " + self.start_date.strftime("%B %Y") + \
               "-" + self.start_date.strftime("%B %Y") + ")"
# end class WorkExperience


class WorkExperience(ExperienceItem):
    """Class for Work/Professional experience"""
# end class WorkExperience


class ExtracurricularExperience(ExperienceItem):
    """Class for listing work done in Concordia, outside of class"""
# end class ExtraCurricularExperience


class VolunteerExperience(ExperienceItem):
    """Class for displaying Volunteer Experience"""
# end class VolunteerExperience

""" ### Section 3 Models ### """


class PersonalProject(DetailedDisplayItem):
    """Class for representing Projects, all Section 3 Items. Can be Active or Inactive/Unsupported """
# end class PersonalProject

""" ### Section 4 Models ### """


class GameTitle(DisplayItem):
    """Proxy Class for all Commercial Games worked on, Section 4 Items"""
    external_link = models.URLField(max_length=200, help_text="Link external site. Inserted as an href", blank=True)
# end class GameTitle

""" ### Section 5 Models ### """


class PersonalInterest(DetailedDisplayItem):
    """Proxy Class for any Hobbies or general interests, These are Section 5 Items"""
# end class PersonalInterest

""" ### Section 6 Models ### """


class ContactInfo(DisplayItem):
    """Class to hold all contact information"""
    external_link = models.CharField(max_length=200, help_text="Link external site. Inserted as an href")
# end class ContactInfo

