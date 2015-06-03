"""
Vanilla product models
"""
from oscar.core.loading import is_model_registered
from oscar.apps.catalogue.abstract_models import *  # noqa

__all__ = ['ProductAttributesContainer']


if not is_model_registered('catalogue', 'ProductClass'):
    class ProductClass(AbstractProductClass):
        pass

    __all__.append('ProductClass')


if not is_model_registered('catalogue', 'Category'):
    class Category(AbstractCategory):
        pass

    __all__.append('Category')


if not is_model_registered('catalogue', 'ProductCategory'):
    class ProductCategory(AbstractProductCategory):
        pass

    __all__.append('ProductCategory')


if not is_model_registered('catalogue', 'Product'):
    class Product(AbstractProduct):
        pass

    __all__.append('Product')


if not is_model_registered('catalogue', 'ProductVariant'):
    class ProductVariant(AbstractProductVariant):
        pass

    __all__.append('ProductVariant')


if not is_model_registered('catalogue', 'ProductRecommendation'):
    class ProductRecommendation(AbstractProductRecommendation):
        pass

    __all__.append('ProductRecommendation')


if not is_model_registered('catalogue', 'Attribute'):
    class Attribute(AbstractAttribute):
        pass

    __all__.append('ProductAttribute')


if not is_model_registered('catalogue', 'AttributeValue'):
    class AttributeValue(AbstractAttributeValue):
        pass

    __all__.append('AttributeValue')


if not is_model_registered('catalogue', 'ProductVariantAttributeValue'):
    class ProductVariantAttributeValue(AbstractProductVariantAttributeValue):
        pass

    __all__.append('ProductVariantAttributeValue')


if not is_model_registered('catalogue', 'Option'):
    class Option(AbstractOption):
        pass

    __all__.append('Option')


if not is_model_registered('catalogue', 'ProductImage'):
    class ProductImage(AbstractProductImage):
        pass

    __all__.append('ProductImage')
