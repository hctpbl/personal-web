# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20150412_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperiencetranslation',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
