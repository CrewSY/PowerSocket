# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_free_delivery',
            field=models.BooleanField(default=True, verbose_name='Is free delivery'),
        ),
    ]
