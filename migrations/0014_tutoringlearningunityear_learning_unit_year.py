# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-20 13:08
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0013_auto_20160613_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutoringlearningunityear',
            name='learning_unit_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.LearningUnitYear'),
            preserve_default=False,
        ),
    ]
