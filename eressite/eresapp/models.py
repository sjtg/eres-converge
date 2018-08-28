# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.db  import models


#News Letter and Blogs
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    BlogImages = models.FileField(upload_to='photos/blog/', blank=False, null=True)
    CreatedDate = models.DateTimeField(
        default=timezone.now
    )
    PublishedDate = models.DateTimeField(
        blank=True, null=True
    )


    def __unicode__(self):
        Title = str(self.Title)
        return Title


#Upload of research papers
class Documents(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    description = models.TextField()
    docs = models.FileField(upload_to='Documents/eres/', blank=False, null=True)
    uploaded_at = models.DateTimeField(User, auto_now_add=True)


    def __unicode__(self):
        title = str(self.title)
        return title


#Upload of research feedback
class Reviewer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    comments= models.TextField()
    docs = models.FileField(upload_to='Documents/research/', blank=False, null=True)
    uploaded_at = models.DateTimeField(User, auto_now_add=True)


    def __unicode__(self):
        title = str(self.title)
        return title

# Fees
class Fees(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    prices = models.IntegerField()


    def __unicode__(self):
        title = str(self.title)
        return title
