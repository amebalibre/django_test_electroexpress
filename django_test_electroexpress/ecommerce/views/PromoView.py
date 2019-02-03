"""Promo View."""
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from ecommerce.models import Invoice
from ecommerce.models import Promo
from ecommerce.serializers import PromoSerializer
from ecommerce.exceptions import NotAcceptableOnPromoModel


class PromoGeneric(object):
    """Generic class that allows data to be CRUD."""

    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
    permission_classes = (permissions.IsAdminUser,)


class PromoList(PromoGeneric, generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    pass


class PromoDetail(PromoGeneric, generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    def destroy(self, request, pk, format=None):
        """Restrict delete if promo is used on invoice."""
        invoices = Invoice.objects.all().filter(
            promos=pk,
            payment_date__isnull=False)

        if(invoices):
            raise NotAcceptableOnPromoModel()

        return Response(status=status.HTTP_204_NO_CONTENT)
