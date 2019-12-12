# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-14 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180504_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
            ],
        ),
    ]