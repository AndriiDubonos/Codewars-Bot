# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CWUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cw_username', models.CharField(max_length=100)),
                ('cw_url', models.CharField(max_length=100)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tasks')),
            ],
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='task',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
