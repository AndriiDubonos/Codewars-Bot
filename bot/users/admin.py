# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import CWUser, Tasks

from django.contrib import admin

# Register your models here.
admin.site.register(CWUser)
admin.site.register(Tasks)
