# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20161018_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='no title', max_length=30),
        ),
    ]
