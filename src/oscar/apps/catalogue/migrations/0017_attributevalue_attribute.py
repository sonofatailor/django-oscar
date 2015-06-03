# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0016_auto_20150603_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributevalue',
            name='attribute',
            field=models.ForeignKey(verbose_name='Attribute', blank=True, to='catalogue.Attribute', null=True),
        ),
    ]
