"""ViewSet Class."""
from rest_framework import viewsets
from ecommerce.models import InvoiceLine
from ecommerce.serializers import InvoiceLineSerializer


class InvoiceLineViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = InvoiceLine.objects.all()
    serializer_class = InvoiceLineSerializer
