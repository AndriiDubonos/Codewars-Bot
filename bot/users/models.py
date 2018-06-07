# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.


class CWUser(models.Model):
    cw_username = models.CharField(max_length=100)
    cw_url = models.CharField(max_length=100)

    def __str__(self):
        return self.cw_username

    @property
    def last_task(self):
        if self.tasks.first():
            return self.tasks.latest('created').name
        else:
            return None


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('users.CWUser', null=True, blank=True, related_name='tasks', on_delete=models.SET_NULL)

    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.name
