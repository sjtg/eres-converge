# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-28 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eresapp', '0008_auto_20180801_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='blog_images',
            new_name='BlogImages',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='CreatedDate',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='PublishedDate',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='Text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='Title',
        ),
    ]
