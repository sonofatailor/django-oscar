# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20150531_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributeoption',
            name='option_color',
            field=models.CharField(max_length=255, null=True, verbose_name='Option Color'),
        ),
    ]
