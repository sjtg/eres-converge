# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin

from django.db.models.signals import post_save

from django.dispatch import receiver

from django.db import models

from django.db  import models

from django.utils import timezone

# Create your models here.

class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     fname = models.CharField(max_length=30, blank=True)
     lname = models.CharField(max_length=30, blank=True)
     email_confirmed = models.BooleanField(default=False)
     cellphone= models.CharField(max_length=30, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.get_or_create(user=instance)
        instance.profile.save()



class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=200)
    text = models.TextField()
    blog_images = models.FileField(upload_to='photos/blog', blank=False, null=True)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __unicode__(self):
        title = str(self.title)
        return title


class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='Documents/')
    uploaded_at = models.DateTimeField(User, auto_now_add=True)
