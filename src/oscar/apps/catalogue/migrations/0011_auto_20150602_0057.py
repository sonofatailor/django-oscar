# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oscar.models.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_auto_20150531_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('code', models.SlugField(max_length=128, verbose_name='Code', validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z\\-_][0-9a-zA-Z\\-_]*$', message="Code can only contain the letters a-z, A-Z, digits, minus and underscores, and can't start with a digit")])),
                ('type', models.CharField(default=b'text', max_length=20, verbose_name='Type', choices=[(b'text', 'Text'), (b'integer', 'Integer'), (b'boolean', 'True / False'), (b'float', 'Float'), (b'richtext', 'Rich Text'), (b'date', 'Date'), (b'option', 'Option'), (b'image', 'Image')])),
                ('required', models.BooleanField(default=False, verbose_name='Required')),
                ('display_order', models.PositiveIntegerField(default=0, help_text='An image with a display order of zero will be the primary image for a product', verbose_name='Display order')),
                ('option_group', models.ForeignKey(blank=True, to='catalogue.AttributeOptionGroup', help_text='Select an option group if using type "Option"', null=True, verbose_name='Option Group')),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
                'verbose_name': 'Product attribute',
                'verbose_name_plural': 'Product attributes',
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value_text', models.TextField(null=True, verbose_name='Text', blank=True)),
                ('value_integer', models.IntegerField(null=True, verbose_name='Integer', blank=True)),
                ('value_boolean', models.NullBooleanField(verbose_name='Boolean')),
                ('value_float', models.FloatField(null=True, verbose_name='Float', blank=True)),
                ('value_richtext', models.TextField(null=True, verbose_name='Richtext', blank=True)),
                ('value_date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('value_image', models.ImageField(max_length=255, null=True, upload_to=b'images/products/%Y/%m/', blank=True)),
                ('attribute', models.ForeignKey(related_name='attribute_values', verbose_name='Attribute', to='catalogue.Attribute')),
                ('value_option', models.ForeignKey(verbose_name='Value option', blank=True, to='catalogue.AttributeValue', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Product attribute value',
                'verbose_name_plural': 'Product attribute values',
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title', blank=True)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('upc', oscar.models.fields.NullCharField(max_length=64, help_text='Universal Product Code (UPC) is an identifier for a product which is not specific to a particular  supplier. Eg an ISBN for a book.', unique=True, verbose_name='UPC')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated', db_index=True)),
                ('display_order', models.PositiveIntegerField(default=0, help_text='An image with a display order of zero will be the primary image for a product', verbose_name='Display order')),
            ],
            options={
                'ordering': ['display_order', '-date_created'],
                'abstract': False,
                'verbose_name': 'Product Variant',
                'verbose_name_plural': 'Product Variants',
            },
        ),
        migrations.CreateModel(
            name='ProductVariantAttributeValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute', models.ForeignKey(verbose_name='Attribute', blank=True, to='catalogue.Attribute', null=True)),
                ('attribute_value', models.ForeignKey(verbose_name='Attribute Value', to='catalogue.AttributeValue')),
                ('product_variant', models.ForeignKey(related_name='attribute_values', verbose_name='Product', blank=True, to='catalogue.ProductVariant', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Product attribute value',
                'verbose_name_plural': 'Product attribute values',
            },
        ),
        migrations.RemoveField(
            model_name='attributeoption',
            name='group',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='option_group',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='product_class',
        ),
        migrations.AlterUniqueTogether(
            name='productattributevalue',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='productattributevalue',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='productattributevalue',
            name='entity_content_type',
        ),
        migrations.RemoveField(
            model_name='productattributevalue',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productattributevalue',
            name='value_option',
        ),
        migrations.RemoveField(
            model_name='product',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='child_images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_options',
        ),
        migrations.RemoveField(
            model_name='product',
            name='structure',
        ),
        migrations.RemoveField(
            model_name='product',
            name='upc',
        ),
        migrations.DeleteModel(
            name='AttributeOption',
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
        migrations.DeleteModel(
            name='ProductAttributeValue',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='attributes',
            field=models.ManyToManyField(help_text='A product attribute is something that this product may have, such as a size, as specified by its class', to='catalogue.Attribute', verbose_name='Attributes', through='catalogue.ProductVariantAttributeValue'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='images',
            field=models.ManyToManyField(related_name='variants', verbose_name='Child images', to='catalogue.ProductImage', blank=b'True'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='parent',
            field=models.ForeignKey(related_name='variants', blank=True, to='catalogue.Product', help_text="Only choose a parent product if you're creating a child product.  For example if this is a size 4 of a particular t-shirt.  Leave blank if this is a stand-alone product (i.e. there is only one version of this product).", null=True, verbose_name='Parent product'),
        ),
        migrations.AddField(
            model_name='productclass',
            name='attributes',
            field=models.ManyToManyField(to='catalogue.Attribute', verbose_name='Attributes', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='productvariantattributevalue',
            unique_together=set([('attribute', 'product_variant', 'attribute_value')]),
        ),
    ]
