# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('personal_site', '0008_auto_20170525_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experienceitem',
            name='display_pictures',
        ),
        migrations.RemoveField(
            model_name='personalinterest',
            name='display_pictures',
        ),
        migrations.RemoveField(
            model_name='personalproject',
            name='display_pictures',
        ),
        migrations.AddField(
            model_name='experienceitem',
            name='improved_display_pictures',
            field=models.ManyToManyField(to='wagtailimages.Image', blank=True, help_text='Relevant images'),
        ),
        migrations.AddField(
            model_name='personalinterest',
            name='improved_display_pictures',
            field=models.ManyToManyField(to='wagtailimages.Image', blank=True, help_text='Relevant images'),
        ),
        migrations.AddField(
            model_name='personalproject',
            name='improved_display_pictures',
            field=models.ManyToManyField(to='wagtailimages.Image', blank=True, help_text='Relevant images'),
        ),
        migrations.DeleteModel(
            name='ImageListField',
        ),
    ]
