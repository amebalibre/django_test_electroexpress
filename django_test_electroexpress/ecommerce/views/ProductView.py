"""Product View."""
from rest_framework import generics
from ecommerce.models import Product
from ecommerce.serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
