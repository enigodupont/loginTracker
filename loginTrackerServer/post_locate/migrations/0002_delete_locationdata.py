# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 05:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_locate', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='locationData',
        ),
    ]
