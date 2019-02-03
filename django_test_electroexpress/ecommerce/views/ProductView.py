"""Product View."""
from rest_framework import generics
from rest_framework import permissions
from ecommerce.models import Product
from ecommerce.serializers import ProductSerializer


class ProductGeneric(object):
    """API endpoint that allows data to be CRUD."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ProductList(ProductGeneric, generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    pass


class ProductDetail(ProductGeneric, generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    pass
