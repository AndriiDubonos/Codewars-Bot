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
		if user.last_task:
			index = last_tasks.index(user.last_task)
		else:
			Tasks.objects.create(name=last_tasks[0], user=user)
			index = 0
		for task in last_tasks[:index]:
			Tasks.objects.create(name=task, user=user)
