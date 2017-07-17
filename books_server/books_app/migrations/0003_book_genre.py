# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-08 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_auto_20170708_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='books_app.Genre', verbose_name='author'),
            preserve_default=False,
        ),
    ]
