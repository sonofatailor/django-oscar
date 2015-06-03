# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0014_auto_20150602_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributevalue',
            name='attribute',
            field=models.ForeignKey(verbose_name='Attribute', blank=True, to='catalogue.Attribute', null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='attributes',
            field=models.ManyToManyField(help_text='A product variant attribute is something that this product may have, such as a size, as specified by its class', to='catalogue.Attribute', verbose_name='Attributes', through='catalogue.ProductVariantAttributeValue'),
        ),
    ]
