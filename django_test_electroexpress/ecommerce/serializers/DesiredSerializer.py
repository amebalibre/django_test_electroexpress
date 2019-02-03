"""Desireds Serializer Class."""
from rest_framework import serializers
from ecommerce.models import Product
from ecommerce.models import Desired
from ecommerce.serializers.ProductSerializer import ProductSerializer


class DesiredSerializer(serializers.ModelSerializer):
    """Desired serialzier.

    Products desired from user.
    """

    product = ProductSerializer(
        many=False,
        read_only=True)

    class Meta:
        """Metadata of serializer."""

        model = Desired
        fields = (
            'owner',
            'product',
        )
        read_only_fields = ('owner',)


class DesiredPutSerializer(serializers.ModelSerializer):
    """Desired serialzier.

    Products desired from user.
    """

    owner = serializers.ReadOnlyField(
        source='owner.username')

    def create(self, validated_data):
        """Create new realation between connected user and product."""
        owner = validated_data.pop('owner')
        product = validated_data.pop('product')
        return Desired.objects.create(owner=owner, product=product)

    class Meta:
        """Metadata of serializer."""

        model = Desired
        fields = (
            'owner',
            'product',
        )


class DesiredCreateSerializer(serializers.ModelSerializer):
    """Desired serialzier.

    Products desired from user.
    """

    owner = serializers.ReadOnlyField(
        source='owner.username')

    product = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        queryset=Product.objects.all())

    def create(self, validated_data):
        """Create new realation between connected user and product."""
        owner = validated_data.pop('owner')
        product = validated_data.pop('product')
        return Desired.objects.create(owner=owner, product=product)

    class Meta:
        """Metadata of serializer."""

        model = Desired
        fields = (
            'owner',
            'product',
        )
