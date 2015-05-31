# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productalert',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, verbose_name='Email', blank=True),
        ),
    ]
