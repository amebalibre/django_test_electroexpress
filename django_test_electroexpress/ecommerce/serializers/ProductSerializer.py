"""Serializer Class."""
from rest_framework import serializers
from ecommerce.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """."""

    type = serializers.CharField(source='get_type_display')

    class Meta:
        """Metadata of serializer."""

        model = Product
        fields = (
            'name',
            'price',
            'type',
            'stock',
            'inclusion_date',
            'discontinued_date',
            'was_discontinued')
