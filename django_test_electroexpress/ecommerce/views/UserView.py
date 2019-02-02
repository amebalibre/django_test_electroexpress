"""User View."""
from django.contrib.auth.models import User
from rest_framework import generics
from ecommerce.serializers import UserSerializer


class UserList(generics.ListAPIView):
    """API endpoint that allows data to be viewed."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """API endpoint that allows data to be retrieve."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
