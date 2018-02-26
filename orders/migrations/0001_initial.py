# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_auto_20180226_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'New'), ('In process', 'In process'), ('Completed', 'Completed'), ('Closed', 'Closed')], default='1', max_length=12, verbose_name='Status')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Total price')),
                ('customer_name', models.CharField(blank=True, max_length=64, verbose_name='Customer name')),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Customer email')),
                ('customer_phone', models.CharField(blank=True, max_length=48, verbose_name='Customer phone')),
                ('customer_address', models.CharField(blank=True, max_length=128, verbose_name='Customer address')),
                ('comments', models.TextField(blank=True, verbose_name='Comments')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='SmartphoneInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, verbose_name='Count')),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Price per item')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Total price')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Order')),
                ('smartphone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Smartphone', verbose_name='Smartphone')),
            ],
            options={
                'verbose_name': 'Smartphone in order',
                'verbose_name_plural': 'Smartphones in orders',
            },
        ),
    ]