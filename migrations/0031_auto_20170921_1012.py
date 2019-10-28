# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-21 08:12
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0156_offeryearentity_education_group_year'),
        ('assistant', '0030_mandateentity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewer',
            name='structure',
        ),
        migrations.AddField(
            model_name='reviewer',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Entity'),
        ),
    ]
