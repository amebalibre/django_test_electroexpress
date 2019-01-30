"""Model Class."""
from django.db import models


class Desired(models.Model):
    """Desired."""

    name = models.CharField(max_length=50)
