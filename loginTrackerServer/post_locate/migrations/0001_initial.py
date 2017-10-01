# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locationData',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('lat', models.TextField(blank=True, max_length=500)),
                ('long', models.TextField(blank=True, max_length=500)),
                ('city', models.TextField(blank=True, max_length=500)),
                ('country_name', models.TextField(blank=True, max_length=500)),
                ('ip', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]
