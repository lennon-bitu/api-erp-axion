from rest_framework.viewsets import ModelViewSet
from .models import Product, Category, ProductVariation
from .serializers import ProductSerializer, CategorySerializer, ProductVariationSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related(
        'images',
        'variations'
    ).select_related('category')

    serializer_class = ProductSerializer


from rest_framework.viewsets import ModelViewSet

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# opcional crud para variações de produtos diretamente
class ProductVariationViewSet(ModelViewSet):
    queryset = ProductVariation.objects.select_related('product')
    serializer_class = ProductVariationSerializer
