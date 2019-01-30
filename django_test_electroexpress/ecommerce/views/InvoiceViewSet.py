"""ViewSet Class."""
from rest_framework import viewsets
from ecommerce.models import Invoice
from ecommerce.serializers import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
