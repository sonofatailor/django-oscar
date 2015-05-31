# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20150529_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributeoption',
            name='option_image',
            field=models.ImageField(max_length=255, null=True, upload_to=b'images/products/%Y/%m/', blank=True),
        ),
        migrations.AddField(
            model_name='attributeoption',
            name='swatch_type',
            field=models.CharField(default=b'text', max_length=255, verbose_name='Swatch Type', choices=[(b'text', 'Text'), (b'color', 'Color'), (b'image', 'Image')]),
        ),
    ]
