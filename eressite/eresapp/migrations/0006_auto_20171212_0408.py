# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 04:08
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eresapp', '0005_auto_20171018_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=django.contrib.auth.models.User),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]