from django.db import models


# Create your models here.
class ExampleItem(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.title

