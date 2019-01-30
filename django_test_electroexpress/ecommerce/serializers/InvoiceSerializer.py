"""Serializer Class."""
from rest_framework import serializers
from ecommerce.models import Invoice
from ecommerce.serializers.InvoiceLineSerializer import InvoiceLineSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    """."""

    lines = InvoiceLineSerializer(source='invoiceline_set', many=True)
    promos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='code'
     )

    class Meta:
        """Metadata of serializer."""

        model = Invoice
        fields = (
            'name',
            'total',
            'total_lines',
            'total_promos',
            'shipping_cost',
            'promos',
            'lines',)
