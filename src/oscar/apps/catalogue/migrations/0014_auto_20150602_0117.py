# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_auto_20150602_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributevalue',
            name='display_order',
            field=models.PositiveIntegerField(default=0, help_text='An image with a display order of zero will be the primary image for a product', verbose_name='Display order'),
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='swatch_type',
            field=models.CharField(default=b'text', max_length=255, verbose_name='Swatch Type', choices=[(b'text', 'Text'), (b'color', 'Color'), (b'image', 'Image')]),
        ),
    ]
