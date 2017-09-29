# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0152_auto_20170905_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationgroup',
            name='uuid',
        ),
        migrations.AddField(
            model_name='educationgroup',
            name='start_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='educationgroup',
            name='end_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='educationgroupyear',
            name='uuid',
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='academic_type',
            field=models.CharField(blank=True, choices=[('NON_ACADEMIC', 'NON_ACADEMIC'), ('NON_ACADEMIC_CREF', 'NON_ACADEMIC_CREF'), ('ACADEMIC', 'ACADEMIC')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='active',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('RE_REGISTRATION', 'RE_REGISTRATION')], default='ACTIVE', max_length=20),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='admission_exam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='diploma_printing_orientation',
            field=models.CharField(blank=True, choices=[('NO_PRINT', 'NO_PRINT'), ('IN_HEADING_2_OF_DIPLOMA', 'IN_HEADING_2_OF_DIPLOMA'), ('IN_EXPECTED_FORM', 'IN_EXPECTED_FORM')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='diploma_printing_title',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='dissertation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='english_activities',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO'), ('OPTIONAL', 'OPTIONAL')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='enrollment_campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='base.Campus'),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='fee_type',
            field=models.CharField(blank=True, choices=[('FEE_1', 'FEE_1'), ('FEE_2', 'FEE_2'), ('FEE_3', 'FEE_3'), ('FEE_4', 'FEE_4'), ('FEE_5', 'FEE_5'), ('FEE_6', 'FEE_6'), ('FEE_7', 'FEE_7'), ('FEE_8', 'FEE_8'), ('FEE_10', 'FEE_10'), ('FEE_11', 'FEE_11'), ('FEE_12', 'FEE_12'), ('FEE_13', 'FEE_13')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='funding',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='funding_cud',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='funding_direction',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='funding_direction_cud',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='inter_organization_information',
            field=models.CharField(blank=True, max_length=320, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='internship',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO'), ('OPTIONAL', 'OPTIONAL')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='joint_diploma',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='main_teaching_campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teaching', to='base.Campus'),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='other_campus_activities',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO'), ('OPTIONAL', 'OPTIONAL')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='other_language_activities',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO'), ('OPTIONAL', 'OPTIONAL')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='partial_deliberation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='professional_title',
            field=models.CharField(blank=True, max_length=320, null=True),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='schedule_type',
            field=models.CharField(choices=[('DAILY', 'DAILY'), ('SHIFTED', 'SHIFTED'), ('ADAPTED', 'ADAPTED')], default='DAILY', max_length=20),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='university_certificate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offeryeardomain',
            name='education_group_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.EducationGroupYear'),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='inter_university_abroad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='inter_university_belgium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='inter_university_french_community',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='educationgroupyear',
            name='primary_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reference.Language'),
        ),
    ]