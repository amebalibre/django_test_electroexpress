"""Model Class."""
from django.db import models


class User(models.Model):
    """User."""

    name = models.CharField(max_length=50)
    # phone =
    # address = models.CharField(max_length=80)  # direccion
