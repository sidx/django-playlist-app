# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genremodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='songmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]