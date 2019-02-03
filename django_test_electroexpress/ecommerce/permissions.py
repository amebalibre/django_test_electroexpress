"""Permissions file."""
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        """Only allowed to the owner of the element."""
        return obj.owner == request.user
