# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_attributevalue_attribute'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'ordering': ['code'], 'verbose_name': 'Attribute', 'verbose_name_plural': 'Attributes'},
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='option_group',
        ),
        migrations.RemoveField(
            model_name='attributevalue',
            name='group',
        ),
        migrations.DeleteModel(
            name='AttributeOptionGroup',
        ),
    ]
