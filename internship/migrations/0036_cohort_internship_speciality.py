# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-03 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid

from internship.models.cohort import Cohort
from internship.models.internship_speciality import InternshipSpeciality


def assign_first_cohort_to_periods(apps, schema_editor):
    cohort = Cohort.objects.first()

    InternshipSpeciality.objects.all().update(cohort=cohort)

class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0035_cohort_organization_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipspeciality',
            name='cohort',
            field=models.ForeignKey(null=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='internship.Cohort'),
            preserve_default=False,
        ),
        migrations.RunPython(assign_first_cohort_to_periods),
        migrations.AlterField(
            model_name='internshipspeciality',
            name='cohort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internship.Cohort'),
            preserve_default=False,
        ),
    ]
