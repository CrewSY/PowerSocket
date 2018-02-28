# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Photo')),
                ('model', models.CharField(blank=True, max_length=255, verbose_name='Model')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Price')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created date')),
                ('in_stock', models.BooleanField(default=True, verbose_name='In stock')),
            ],
            options={
                'verbose_name': 'Smartphone',
                'verbose_name_plural': 'Smartphones',
            },
        ),
        migrations.CreateModel(
            name='SmartphoneBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=64, verbose_name='Brand')),
            ],
            options={
                'verbose_name': 'Smartphone Brand',
                'verbose_name_plural': 'Smartphone Brands',
            },
        ),
        migrations.AddField(
            model_name='smartphone',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.SmartphoneBrand', verbose_name='Brand'),
        ),
    ]
