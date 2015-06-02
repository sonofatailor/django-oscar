# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_auto_20150602_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributevalue',
            name='attribute',
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='value_option',
            field=models.ForeignKey(related_name='option_values', verbose_name='Value option', blank=True, to='catalogue.AttributeOptionGroup', null=True),
        ),
    ]
