# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('personal_site', '0007_auto_20160531_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exampleitem',
            name='list_images',
        ),
        migrations.AddField(
            model_name='exampleitem',
            name='list_images_new',
            field=models.ManyToManyField(blank=True, to='wagtailimages.Image'),
        ),
    ]
