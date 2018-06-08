# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django
django.setup()

from parser import parse_url
from users.models import CWUser, Tasks


def parsing():
	users = CWUser.objects.all()
	for user in users:
		last_tasks = parse_url(user.cw_url)
		for task in last_tasks:
			if task in [str(i) for i in user.tasks.all()]:
				pass
			else:
				Tasks.objects.create(name=task, user=user)
