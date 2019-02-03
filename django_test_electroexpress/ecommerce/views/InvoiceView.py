"""Invoice View."""
from rest_framework import generics
from ecommerce.models import Invoice
from ecommerce.models import InvoiceLine
from ecommerce.serializers.InvoiceSerializer import InvoiceSerializer
from ecommerce.serializers.InvoiceSerializer import InvoiceCreateSerializer
from ecommerce.serializers import LineSerializer


class InvoiceGeneric(object):
    """Generic class that allows data to be CRUD."""

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class LineGeneric(object):
    """Generic class that allows data to be CRUD."""

    queryset = InvoiceLine.objects.all()
    serializer_class = LineSerializer


class InvoiceList(InvoiceGeneric, generics.ListAPIView):
    """API endpoint that allows data to be viewed."""

    pass


class InvoiceCreate(InvoiceGeneric, generics.CreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    serializer_class = InvoiceCreateSerializer


class InvoiceDetail(InvoiceGeneric, generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    pass


class LineList(LineGeneric, generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    pass


class LineDetail(LineGeneric, generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    pass
