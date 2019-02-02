"""Invoices Serializer Class."""
from rest_framework import serializers
from ecommerce.models import Invoice
from ecommerce.models import InvoiceLine
from ecommerce.models import Product
from ecommerce.serializers.ProductSerializer import ProductSerializer


class LineSerializer(serializers.HyperlinkedModelSerializer):
    """Line serializer.

    the lines allow you to assign multiple
    products of the same type to an invoice.
    """

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


class InvoiceSerializer(serializers.ModelSerializer):
    """Invoice serializer."""

    lines = LineSerializer(
        source='invoiceline_set',
        many=True)

    promos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='code')

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
            'lines',
        )
        read_only_fields = ('name',)


class InvoiceCreateSerializer(serializers.ModelSerializer):
    """Invoice serializer."""

    def create(self, validated_data):
        """Generate lines for invoice."""
        products = validated_data.pop('lines')
        invoice = Invoice.objects.create(**validated_data)
        try:
            for product in products:
                InvoiceLine.objects.create(invoice=invoice, product=product)
        except TypeError as e:
            print(e)
            invoice.delete()
        else:
            return invoice

    lines = serializers.SlugRelatedField(
        slug_field='id',
        many=True,
        queryset=Product.objects.all()
    )
    promos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='code')

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
            'lines',
        )
        read_only_fields = ('name',)
