"""Model Class."""
from django.db import models
from django.db.models import Q


class Desired(models.Model):
    """Desired."""

    owner = models.ForeignKey(
        to='auth.User',
        related_name='desireds',
        on_delete=models.CASCADE)

    product = models.ForeignKey(
        to='Product',
        related_name='product',
        on_delete=models.CASCADE,
        limit_choices_to=Q(stock__gt=0))
