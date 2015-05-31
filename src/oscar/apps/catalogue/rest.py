from wq.db import rest
from oscar.core.loading import get_model
from .serializers import ProductSerializer


ProductClass = get_model('catalogue', 'ProductClass')
Category = get_model('catalogue', 'Category')
ProductCategory = get_model('catalogue', 'ProductCategory')
Product = get_model('catalogue', 'Product')
ProductRecommendation = get_model('catalogue', 'ProductRecommendation')

rest.router.register_model(ProductClass)
rest.router.register_model(Product, serializer=ProductSerializer, queryset=Product.objects.all().select_related('product_class', 'parent').prefetch_related('attribute_values', 'attribute_values__attribute'))
rest.router.register_model(Category)
