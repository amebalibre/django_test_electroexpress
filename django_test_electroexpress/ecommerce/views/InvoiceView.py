"""Invoice View."""
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from ecommerce.models import Invoice
from ecommerce.models import InvoiceLine
from ecommerce.serializers.InvoiceSerializer import InvoiceSerializer
from ecommerce.serializers import LineSerializer
import ecommerce.permissions as custom_permissions
from ecommerce.exceptions import NotAcceptableOnInvoiceModel


# Invoices
class InvoiceGeneric(object):
    """Generic class that allows data to be CRUD."""

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (custom_permissions.IsOwner,)


class InvoiceList(InvoiceGeneric, generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed."""

    def get_queryset(self):
        """Return all desireds of connected user."""
        return Invoice.objects.all().filter(owner=self.request.user.id)

    def perform_create(self, serializer):
        """Allow us to modify how the instance save is managed."""
        serializer.save(owner=self.request.user)


class InvoiceDetail(InvoiceGeneric, generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    def destroy(self, request, pk, format=None):
        """Restrict delete if invoice is payed."""
        invoice = get_object_or_404(self.queryset, pk=pk)
        if(invoice.payment_date):
            raise NotAcceptableOnInvoiceModel()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Lines
class LineGeneric(object):
    """Generic class that allows data to be CRUD."""

    queryset = InvoiceLine.objects.all()
    serializer_class = LineSerializer


class LineList(LineGeneric, generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    pass


class LineDetail(LineGeneric, generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    pass
