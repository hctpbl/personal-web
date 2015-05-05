# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20150412_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsubcategorytranslation',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
