"""Product View."""
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from ecommerce.models import Invoice
from ecommerce.models import Product
from ecommerce.serializers import ProductSerializer
from ecommerce.exceptions import NotAcceptableOnInvoiceModel


class ProductGeneric(object):
    """Generic class that allows data to be CRUD."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ProductList(ProductGeneric, generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    pass


class ProductDetail(ProductGeneric, generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    def destroy(self, request, pk, format=None):
        """Restrict delete if invoice is associated and is payed."""
        invoices = Invoice.objects.all().filter(
            lines=pk,
            payment_date__isnull=False)

        if(invoices):
            raise NotAcceptableOnInvoiceModel()
        return Response(status=status.HTTP_204_NO_CONTENT)
