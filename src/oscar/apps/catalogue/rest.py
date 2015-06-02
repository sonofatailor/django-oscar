from wq.db import rest
from oscar.core.loading import get_model
from .view_sets import ProductViewSet
from serializers import ProductSerializer


ProductClass = get_model('catalogue', 'ProductClass')
Category = get_model('catalogue', 'Category')
ProductCategory = get_model('catalogue', 'ProductCategory')
Product = get_model('catalogue', 'Product')
ProductRecommendation = get_model('catalogue', 'ProductRecommendation')

rest.router.register_model(ProductClass)
rest.router.register_model(Product, viewset=ProductViewSet, serializer=ProductSerializer)
rest.router.register_model(Category)
