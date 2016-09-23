from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from colorful.fields import RGBColorField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    tutorial = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    color=RGBColorField(default='#0B70DC')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


