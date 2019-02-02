"""Invoice View."""
from rest_framework import generics
from ecommerce.models import Invoice
from ecommerce.models import InvoiceLine
from ecommerce.serializers import InvoiceSerializer
from ecommerce.serializers import LineSerializer


class InvoiceList(generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed."""

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class LineList(generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed."""

    queryset = InvoiceLine.objects.all()
    serializer_class = LineSerializer


class LineDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    queryset = InvoiceLine.objects.all()
    serializer_class = LineSerializer
