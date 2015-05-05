# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20150412_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='skillcategorytranslation',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='skillcategorytranslation',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='skillsubcategorytranslation',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='skillsubcategorytranslation',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
