# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0007_region_parent_segment_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedlabel',
            name='segment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Segment'),
        ),
    ]
