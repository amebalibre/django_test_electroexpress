"""Promos Serializer Class."""
from rest_framework import serializers
from ecommerce.models import Invoice
from ecommerce.models import Promo
from ecommerce.exceptions import NotAcceptableOnPromoModel


class PromoSerializer(serializers.HyperlinkedModelSerializer):
    """Promo serialzier.

    There are two types of products right now. tablets and mobiles.
    """

    def update(self, instance, validated_data):
        """Update the promo if isn't used from payed invoice."""
        invoices = Invoice.objects.all().filter(
            promos=instance.pk,
            payment_date__isnull=False)

        if(invoices):
            raise NotAcceptableOnPromoModel()

        instance.type = validated_data.pop('type', instance.type)
        instance.code = validated_data.pop('code', instance.code)
        instance.value = validated_data.pop('value', instance.value)
        return instance

    class Meta:
        """Metadata of serializer."""

        model = Promo
        fields = (
            'code',
            'type',
            'value',
            'active',
        )
