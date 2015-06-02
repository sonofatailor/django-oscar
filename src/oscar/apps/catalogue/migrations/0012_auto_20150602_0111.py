# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20150602_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributevalue',
            name='value_option',
            field=models.ForeignKey(verbose_name='Value option', blank=True, to='catalogue.AttributeOptionGroup', null=True),
        ),
        migrations.AlterField(
            model_name='productvariantattributevalue',
            name='attribute_value',
            field=models.ForeignKey(related_name='attribute_values', verbose_name='Attribute Value', to='catalogue.AttributeValue'),
        ),
    ]
