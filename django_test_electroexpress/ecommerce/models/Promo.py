"""Model Class."""
from django.db import models


class Promo(models.Model):
    """Promotional discount codes applicable to products."""

    PERCENT = 'P'
    COMPLETE = 'C'
    TYPE_CHOICES = (
        (PERCENT, 'Percent'),
        (COMPLETE, 'Complete'))

    code = models.CharField(
        max_length=10)

    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=PERCENT)

    value = models.IntegerField()
    active = models.BooleanField(
        default=True)

    def __str__(self):
        """Verbose object."""
        if(self.type == self.PERCENT):
            t = '%'
        else:
            t = '€'
        return '{code} ({value}{type})'.format(
            code=self.code,
            value=self.value,
            type=t)

    class Meta:
        """Meta data."""

        ordering = ('type', 'value', 'code',)
