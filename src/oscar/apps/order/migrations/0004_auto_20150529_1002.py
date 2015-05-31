# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20150113_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='guest_email',
            field=models.EmailField(max_length=254, verbose_name='Guest email address', blank=True),
        ),
    ]
