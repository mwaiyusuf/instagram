# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-29 07:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_profile_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='images',
        ),
    ]
