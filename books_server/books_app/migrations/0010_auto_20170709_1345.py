# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-09 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0009_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('a', 'aaa'), ('b', 'bbb'), ('c', 'ccc')], max_length=2),
        ),
    ]