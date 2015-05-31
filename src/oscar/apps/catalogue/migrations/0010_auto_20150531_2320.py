# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_auto_20150531_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributeoption',
            name='option_text',
            field=models.CharField(default=b'', max_length=255, verbose_name='Option Text'),
        ),
    ]
