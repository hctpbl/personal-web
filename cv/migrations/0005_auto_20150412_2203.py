# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20150412_1758'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='skillsubcategorytranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='skillsubcategorytranslation',
            name='master',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='SkillSubCategory',
        ),
        migrations.DeleteModel(
            name='SkillSubCategoryTranslation',
        ),
    ]
