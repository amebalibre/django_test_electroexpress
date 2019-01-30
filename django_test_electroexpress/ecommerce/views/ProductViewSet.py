"""ViewSet Class."""
from rest_framework import viewsets
from ecommerce.models import Product
from ecommerce.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
