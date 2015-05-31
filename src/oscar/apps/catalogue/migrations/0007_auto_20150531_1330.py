# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20150530_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributeoption',
            name='display_order',
            field=models.PositiveIntegerField(default=0, help_text='An image with a display order of zero will be the primary image for a product', verbose_name='Display order'),
        ),
        migrations.AddField(
            model_name='product',
            name='child_images',
            field=models.ManyToManyField(related_name='variants', verbose_name='Child images', to='catalogue.ProductImage', blank=b'True'),
        ),
    ]
