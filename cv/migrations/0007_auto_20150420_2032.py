# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20150420_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicexperiencetranslation',
            name='further_info',
            field=models.TextField(blank=True, default=''),
        ),
    ]
