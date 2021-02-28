# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.conf import settings
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200)
    tools = models.CharField(max_length=100) # space-separated values
    pub_date = models.DateTimeField()
    img_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

def badges_path():
    return os.path.join(settings.STATIC_ROOT, 'mainpage', 'images', 'badges')

class Badge(models.Model):
    """
    A simple name, link and a (path to a) picture. Order is used to order
    badges in template.
    """
    order = models.IntegerField()  # 207 = fila 2, columna 7.
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    link = models.URLField()
    img = models.FilePathField(path=badges_path)
    comments = models.TextField(blank=True)

    def __str__(self):
      return "{} [{:03}]".format(self.name, self.order)
