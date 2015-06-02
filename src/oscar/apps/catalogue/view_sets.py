from wq.db.rest.views import ModelViewSet
from serializers import ProductSerializer
from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().select_related('product_class', 'parent').prefetch_related('attribute_values', 'attribute_values__attribute')
