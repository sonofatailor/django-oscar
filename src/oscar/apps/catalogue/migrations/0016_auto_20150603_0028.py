# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_auto_20150603_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productvariantattributevalue',
            options={'verbose_name': 'Product variant attribute value', 'verbose_name_plural': 'Product variant attribute values'},
        ),
        migrations.RemoveField(
            model_name='attributevalue',
            name='attribute',
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='group',
            field=models.ForeignKey(related_name='attribute_values', default='', verbose_name='Group', to='catalogue.AttributeOptionGroup'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attributevalue',
            name='value_option',
            field=models.ForeignKey(related_name='attribute_values', verbose_name='Value option', blank=True, to='catalogue.AttributeValue', null=True),
        ),
        migrations.AlterField(
            model_name='productvariantattributevalue',
            name='attribute_value',
            field=models.ForeignKey(verbose_name='Attribute Value', to='catalogue.AttributeValue'),
        ),
    ]
