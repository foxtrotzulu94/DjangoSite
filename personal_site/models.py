from django.db import models
from datetime import date
from django.core.files.storage import FileSystemStorage

# path = os.path.join(ROOT_DIR, 'web-private')
# fs = FileSystemStorage(location='/static/personal_site/images/')


class ImageListField(models.Model):
    """Class for linking a Model to a list of Images"""
    img = models.ImageField(upload_to='media/')

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
    subtitle = models.CharField(max_length=30, blank=True)
    thumbnail = models.ImageField(upload_to='media/', blank=True)

    class Meta:
        abstract = True
# end class DisplayItem


class ExperienceItem(DisplayItem):
    """Abstract Class used to model/define Experience items"""

    tech_used = models.CharField(max_length=200)  # Some day, we can make this come from a "tech" table. Not today...
    description = models.TextField()
    display_pictures = models.ManyToManyField(ImageListField,  blank=True)

    # These are displayed differently on the View depending on which subclass they are
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today, blank=True)  # This one could be blank if it is still current.

    def __str__(self):
        return self.title+" ("+self.start_date.strftime("%B %Y")+"-"+self.start_date.strftime("%B %Y")+")"

    # class Meta:
    #     abstract = True
# end class


class WorkExperience(ExperienceItem):
    """Proxy Class for Work, part of Section 2 Items"""
    # title corresponds to Position in this case
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    # URL to the external site
    ext_url = models.URLField(blank=True)

    def __str__(self):
        return self.title + " at " + self.company + " (" + self.location + " | " + self.start_date.strftime("%B %Y") + "-" + self.start_date.strftime("%B %Y") + ")"

# end class WorkExperience


class ExtracurricularExperience(WorkExperience):
    """Class for listing work done in Concordia outside of class"""
    class Meta:
        proxy = True
# end class ExtraCurricularExperience


class VolunteerExperience(WorkExperience):
    """Class for displaying Volunteer Experience and external links"""
    class Meta:
        proxy = True
# enc class VolunteerExperience


class PersonalProject(ExperienceItem):
    """Class for representing Projects, all Section 3 Items. Can be Active or Inactive/Unsupported """
    # TODO: Decide whether projects should include a bool field to mark their activity
    class Meta:
        proxy = True

# end class Projects


class GameTitle(ExperienceItem):
    """Proxy Class for all Commercial Games worked on, Section 4 Items"""

    class Meta:
        proxy = True

# end class CommercialGames


class PersonalInterest(ExperienceItem):
    """Proxy Class for any Hobbies or general interests, These are Section 5 Items"""

    class Meta:
        proxy = True

# end class Hobbies


