# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.db import models

# Create your models here.
class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     FirstName = models.CharField(max_length=30, blank=True)
     LastName = models.CharField(max_length=30, blank=True)
     email_confirmed = models.BooleanField(default=False)
     cellphone= models.CharField(max_length=30, blank=True)
     created_date = models.DateTimeField(
         default=timezone.now
     )


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get_or_create(user=instance)
        instance.profile.save()
