from wq.db.rest.serializers import ModelSerializer
from oscar.core.loading import get_model
from rest_framework import serializers

Product = get_model('catalogue', 'Product')
ProductClass = get_model('catalogue', 'ProductClass')
ProductCategory = get_model('catalogue', 'ProductCategory')
# ProductAttribute = get_model('catalogue', 'ProductAttribute')
# ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')


# class ProductAttributeValueSerializer(ModelSerializer):
#     name = serializers.StringRelatedField(source="attribute")
#     value = serializers.StringRelatedField()
#     value_swatch_type = serializers.StringRelatedField()

#     add_label_fields = False

#     class Meta:
#         model = ProductAttributeValue
#         fields = ('name', 'value', 'value_swatch_type')


# class ProductAttributeSerializer(ModelSerializer):
#     productattributevalue_set = ProductAttributeValueSerializer(many=True)
#     add_label_fields = False

#     class Meta:
#         model = ProductAttribute
#         fields = ('name', 'productattributevalue_set')


class ProductSerializer(ModelSerializer):
    # attribute_values = ProductAttributeValueSerializer(many=True, required=False)
    # categories = serializers.StringRelatedField(many=True, required=False)
    add_label_fields = False
