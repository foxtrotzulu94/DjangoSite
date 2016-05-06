from django.db import models
from django.core.files.storage import FileSystemStorage

# path = os.path.join(ROOT_DIR, 'web-private')
# fs = FileSystemStorage(location='/static/personal_site/images/')


class ImageModel(models.Model):
    """Class for linking a Model to a list of Images"""
    img = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.img.name+" - ("+str(self.img.width)+"x"+str(self.img.height)+")"
# end class ImageModel


class ExampleItem(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    img = models.ImageField(upload_to='media/')  # TODO: Remove in production server

    def __str__(self):
        return self.title
# end class


class DisplayItem(models.Model):
    """Class representing a generic, displayable element"""

    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='media/')
# end class DisplayItem


class ExperienceItem(DisplayItem):
    """Class used to hold Experience items"""

    tech_used = models.CharField(max_length=200)
    description = models.TextField()
    display_pictures = models.ManyToManyField(ImageModel)
# end class


class Projects(ExperienceItem):
    """Proxy Class for Website Section on Projects"""

    class Meta:
        proxy = True

# end class Projects


class WorkExperience(models.Model):
    pass



