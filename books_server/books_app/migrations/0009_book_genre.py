# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-09 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0008_auto_20170709_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('a', 'aaa'), ('b', 'bbb'), ('c', 'ccc')], default='a', max_length=1),
            preserve_default=False,
        ),
    ]
