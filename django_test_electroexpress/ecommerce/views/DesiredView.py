"""Desired View."""
from rest_framework import generics
from ecommerce.models import Desired
from ecommerce.serializers.DesiredSerializer import DesiredSerializer
from ecommerce.serializers.DesiredSerializer import DesiredDetailSerializer
import ecommerce.permissions as custom_permissions


class DesiredGeneric(object):
    """Generic class that allows data to be CRUD."""

    queryset = Desired.objects.all()
    serializer_class = DesiredSerializer
    permission_classes = (custom_permissions.IsOwner,)


class DesiredList(DesiredGeneric, generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    def get_queryset(self):
        """Return all desireds of connected user."""
        return Desired.objects.all().filter(owner=self.request.user.id)


class DesiredDetail(DesiredGeneric, generics.RetrieveDestroyAPIView):
    """API endpoint that allows data to be retrieve or destroyed."""

    pass


class DesiredCreate(DesiredGeneric, generics.CreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    serializer_class = DesiredDetailSerializer

    def perform_create(self, serializer):
        """Allow us to modify how the instance save is managed."""
        serializer.save(owner=self.request.user)


class DesiredPut(DesiredGeneric, generics.UpdateAPIView):
    """API endpoint that allows data to be viewed or created."""

    serializer_class = DesiredDetailSerializer

    def perform_create(self, serializer):
        """Allow us to modify how the instance save is managed."""
        serializer.save(owner=self.request.user)
