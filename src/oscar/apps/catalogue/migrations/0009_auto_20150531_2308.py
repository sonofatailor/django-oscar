# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_attributeoption_option_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributeoption',
            name='option',
        ),
        migrations.AddField(
            model_name='attributeoption',
            name='option_text',
            field=models.CharField(max_length=255, null=True, verbose_name='Option Text'),
        ),
    ]
