# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicExperience',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default='', blank=True, null=True)),
                ('grade', models.DecimalField(default='', decimal_places=2, blank=True, null=True, max_digits=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AcademicExperienceTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('degree', models.CharField(max_length=60)),
                ('institution', models.CharField(max_length=30)),
                ('further_info', models.CharField(default='', max_length=100, blank=True, null=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='cv.AcademicExperience', related_name='translations', null=True, editable=False)),
            ],
            options={
                'db_table': 'cv_academicexperience_translation',
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.CharField(serialize=False, max_length=4, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='cv.Location', related_name='translations', null=True, editable=False)),
            ],
            options={
                'db_table': 'cv_location_translation',
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(serialize=False, max_length=4, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=1000, blank=True, null=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='cv.Project', related_name='translations', null=True, editable=False)),
            ],
            options={
                'db_table': 'cv_project_translation',
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('expertise_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillCategoryTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(default='', max_length=30, blank=True, null=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='cv.SkillCategory', related_name='translations', null=True, editable=False)),
            ],
            options={
                'db_table': 'cv_skillcategory_translation',
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillSubCategory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillSubCategoryTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(default='', max_length=30, blank=True, null=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='cv.SkillSubCategory', related_name='translations', null=True, editable=False)),
            ],
            options={
                'db_table': 'cv_skillsubcategory_translation',
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('company', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default='', blank=True, null=True)),
                ('location', models.ForeignKey(to='cv.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkExperienceTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('role', models.CharField(max_length=50)),
                ('description', models.CharField(default='', max_length=1000, blank=True, null=True)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='cv.WorkExperience', related_name='translations', null=True, editable=False)),
            ],
            options={
                'db_table': 'cv_workexperience_translation',
                'db_tablespace': '',
                'managed': True,
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(to='cv.SkillCategory'),
        ),
        migrations.AddField(
            model_name='skill',
            name='subcategory',
            field=models.ForeignKey(to='cv.SkillSubCategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='cv.Skill'),
        ),
        migrations.AddField(
            model_name='academicexperience',
            name='location',
            field=models.ForeignKey(to='cv.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='workexperiencetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='skillsubcategorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='skillcategorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='projecttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='locationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='academicexperiencetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
