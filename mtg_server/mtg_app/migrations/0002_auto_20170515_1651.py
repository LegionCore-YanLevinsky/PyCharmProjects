# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtg_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='img',
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(upload_to='img', verbose_name='image'),
        ),
    ]