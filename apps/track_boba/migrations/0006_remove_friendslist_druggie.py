# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track_boba', '0005_friendslist_friend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendslist',
            name='druggie',
        ),
    ]
