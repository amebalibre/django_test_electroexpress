"""Desireds Serializer Class."""
from django.db.models import Q
from rest_framework import serializers
from ecommerce.models import Product
from ecommerce.models import Desired
from ecommerce.exceptions import ServerErrorOnCreate


class DesiredSerializer(serializers.ModelSerializer):
    """Desired List and detail serialzier.

    Products desired from user.
    """

    product = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        queryset=Product.objects.all().filter(Q(stock__gt=0)))

    def create(self, validated_data):
        """Create new realation between connected user and product."""
        owner = validated_data.pop('owner')
        product = validated_data.pop('product')
        try:
            return Desired.objects.create(owner=owner, product=product)
        except TypeError:
            raise ServerErrorOnCreate()

    class Meta:
        """Metadata of serializer."""

        model = Desired
        fields = (
            'owner',
            'product',
        )
        read_only_fields = ('owner',)
