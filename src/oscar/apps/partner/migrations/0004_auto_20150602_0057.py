# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20150602_0057'),
        ('partner', '0003_auto_20150529_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockrecord',
            name='product',
        ),
        migrations.AddField(
            model_name='stockrecord',
            name='product_variant',
            field=models.ForeignKey(related_name='stockrecords', default='1', verbose_name='Product', to='catalogue.ProductVariant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stockrecord',
            name='partner',
            field=models.ForeignKey(related_name='stockrecords', verbose_name='Partner', to='partner.Partner', null=True),
        ),
    ]
