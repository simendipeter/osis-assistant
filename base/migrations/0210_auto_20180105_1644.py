# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-05 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0209_auto_20180103_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academiccalendar',
            name='reference',
            field=models.CharField(blank=True, choices=[('DELIBERATION', 'DELIBERATION'), ('DISSERTATION_SUBMISSION', 'DISSERTATION_SUBMISSION'), ('EXAM_ENROLLMENTS', 'EXAM_ENROLLMENTS'), ('SCORES_EXAM_DIFFUSION', 'SCORES_EXAM_DIFFUSION'), ('SCORES_EXAM_SUBMISSION', 'SCORES_EXAM_SUBMISSION'), ('TEACHING_CHARGE_APPLICATION', 'TEACHING_CHARGE_APPLICATION'), ('COURSE_ENROLLMENT', 'COURSE_ENROLLMENT'), ('SUMMARY_COURSE_SUBMISSION', 'SUMMARY_COURSE_SUBMISSION')], max_length=50, null=True),
        ),
    ]
