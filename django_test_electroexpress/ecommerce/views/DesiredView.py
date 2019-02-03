"""Desired View."""
from rest_framework import generics
from rest_framework import permissions
from ecommerce.models import Desired
from ecommerce.serializers.DesiredSerializer import DesiredSerializer
from ecommerce.serializers.DesiredSerializer import DesiredCreateSerializer
from ecommerce.serializers.DesiredSerializer import DesiredPutSerializer
import ecommerce.permissions as custom_permissions


class DesiredPermissions(object):
    """Commons permissions settings."""

    queryset = Desired.objects.all()

    permission_classes = (
        permissions.IsAuthenticated,
        custom_permissions.IsOwner)


class DesiredList(DesiredPermissions, generics.ListAPIView):
    """API endpoint that allows data to be viewed or created."""

    serializer_class = DesiredSerializer

    def get_queryset(self):
        """Return all desireds of connected user."""
        return Desired.objects.all().filter(owner=self.request.user.id)


class DesiredPut(DesiredPermissions, generics.UpdateAPIView):
    """API endpoint that allows data to be updated."""

    serializer_class = DesiredPutSerializer

    def perform_create(self, serializer):
        """Allow us to modify how the instance save is managed."""
        serializer.save(owner=self.request.user)


class DesiredCreate(DesiredPermissions, generics.CreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    serializer_class = DesiredCreateSerializer

    def perform_create(self, serializer):
        """Allow us to modify how the instance save is managed."""
        serializer.save(owner=self.request.user)


class DesiredDetail(DesiredPermissions, generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    serializer_class = DesiredSerializer
