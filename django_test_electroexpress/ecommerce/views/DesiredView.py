"""Desired View."""
from rest_framework import generics
from rest_framework import permissions
from ecommerce.models import Desired
from ecommerce.serializers import DesiredSerializer
from ecommerce.serializers.DesiredSerializer import DesiredCreateSerializer
import ecommerce.permissions as custom_permissions


class DesiredList(generics.ListAPIView):
    """API endpoint that allows data to be viewed or created."""

    serializer_class = DesiredSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        custom_permissions.IsOwner)

    def get_queryset(self):
        """Return all desireds of connected user."""
        return Desired.objects.all().filter(owner=self.request.user.id)


class DesiredCreate(generics.CreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    queryset = Desired.objects.all()
    serializer_class = DesiredCreateSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        custom_permissions.IsOwner)

    def perform_create(self, serializer):
        """Allow us to modify how the instance save is managed."""
        serializer.save(owner=self.request.user)


class DesiredDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    queryset = Desired.objects.all()
    serializer_class = DesiredSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        custom_permissions.IsOwner)
