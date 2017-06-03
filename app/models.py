from django.db import models
from datetime import datetime
from random import choice

import string


class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


def generate_key():
    chars = string.digits + string.ascii_letters
    return ''.join(choice(chars) for _ in range(3))


class ShortUrl(models.Model):
    key = models.CharField(max_length=4, primary_key=True, default=generate_key)
    target = models.URLField(max_length=255, null=False, blank=True, unique=True)
    added = models.DateTimeField(auto_now_add=True, editable=False)


def __unicode__(self):
    return '%s %s' % (self.target, self.key)


class Hit(models.Model):
    target = models.ForeignKey(ShortUrl)
    time = models.DateTimeField(auto_now_add=True, editable=False)
    referer = models.URLField(blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(blank=True, max_length=100)