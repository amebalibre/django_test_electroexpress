"""Invoices Serializer Class."""
from django.db.models import Q
from rest_framework import serializers
from ecommerce.models import Invoice
from ecommerce.models import InvoiceLine
from ecommerce.models import Product
from ecommerce.models import Promo
from ecommerce.serializers.ProductSerializer import ProductSerializer
from ecommerce.exceptions import NotAcceptableOnInvoiceModel
from ecommerce.exceptions import ServerErrorOnCreate


# Lines
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


# Invoices
class InvoiceSerializer(serializers.ModelSerializer):
    """Invoice serializer."""

    lines = serializers.SlugRelatedField(
        slug_field='id',
        many=True,
        queryset=Product.objects.all().filter(Q(stock__gt=0))
    )

    promos = serializers.SlugRelatedField(
        slug_field='id',
        many=True,
        queryset=Promo.objects.all()
    )

    def create(self, validated_data):
        """Generate lines for invoice."""
        products = validated_data.pop('lines')
        promos = validated_data.pop('promos')
        invoice = Invoice.objects.create(**validated_data)
        try:
            for product in products:
                InvoiceLine.objects.create(invoice=invoice, product=product)
            invoice.promos.set(promos)
        except TypeError:
            invoice.delete()
            raise ServerErrorOnCreate()
        else:
            return invoice

    def update(self, instance, validated_data):
        """Update the invoice relations and promos and shipping cost."""
        if(instance.payment_date):
            raise NotAcceptableOnInvoiceModel()
        products = validated_data.pop('lines')
        promos = validated_data.pop('promos')

        instance.invoiceline_set.all().delete()
        for product in products:
            line = InvoiceLine.objects.create(
                invoice=instance,
                product=product)
            instance.invoiceline_set.add(line)

        instance.promos.set(promos)
        instance.shipping_cost = \
            validated_data.get('shipping_cost', instance.shipping_cost)
        instance.payment_date = \
            validated_data.get('payment_date', instance.payment_date)

        return instance

    class Meta:
        """Metadata of serializer."""

        model = Invoice
        fields = (
            'name',
            'payment_date',
            'total',
            'total_lines',
            'total_promos',
            'shipping_cost',
            'promos',
            'lines',
        )
        read_only_fields = ('name',)
