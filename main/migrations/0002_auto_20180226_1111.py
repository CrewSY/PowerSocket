# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='model',
            field=models.CharField(blank=True, max_length=255, verbose_name='Model'),
        ),
    ]
