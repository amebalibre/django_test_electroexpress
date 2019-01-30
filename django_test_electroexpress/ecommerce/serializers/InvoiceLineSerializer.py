"""Serializer Class."""
from rest_framework import serializers
from ecommerce.models import InvoiceLine
from ecommerce.serializers.ProductSerializer import ProductSerializer


class InvoiceLineSerializer(serializers.HyperlinkedModelSerializer):
    """."""

    product = ProductSerializer()

    class Meta:
        """Metadata of serializer."""

        model = InvoiceLine
        fields = (
            'quantity',
            'price',
            'total',
            'product',
        )
