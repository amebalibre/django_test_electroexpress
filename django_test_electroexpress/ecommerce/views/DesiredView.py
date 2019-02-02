"""Desired View."""
from rest_framework import generics
from rest_framework import permissions
from ecommerce.models import Desired
from ecommerce.serializers import DesiredSerializer


class DesiredList(generics.ListCreateAPIView):
    """API endpoint that allows data to be viewed or created."""

    queryset = Desired.objects.all()
    serializer_class = DesiredSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """Allow us to modify how the instance save is managed."""
        serializer.save(owner=self.request.user)


class DesiredDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that allows data to be retrieve, updated or destroyed."""

    queryset = Desired.objects.all()
    serializer_class = DesiredSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
