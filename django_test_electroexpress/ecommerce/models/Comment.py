"""Model Class."""
from django.db import models
from datetime import date


class Comment(models.Model):
    """Comment."""

    comment = models.CharField(
        max_length=50)

    assessment = models.IntegerField()

    post_date = models.DateField(
        default=date.today)

    class Meta:
        """Meta data."""

        ordering = ('post_date',)
