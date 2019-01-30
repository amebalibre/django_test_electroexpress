"""Model Class."""
from django.db import models
from datetime import date


class Product(models.Model):
    """The products represent tablets or mobiles."""

    TABLET = 'T'
    MOBILE = 'M'
    TYPE_CHOICES = (
        (TABLET, 'Tablet'),
        (MOBILE, 'Mobile'))

    name = models.CharField(
        max_length=80)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2)

    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=MOBILE)

    stock = models.IntegerField(default=99)

    inclusion_date = models.DateField(
        default=date.today())

    discontinued_date = models.DateField(
        null=True,
        blank=True,
    )

    @property
    def was_discontinued(self):
        """Check if product was discontinued or not."""
        return (
            self.discontinued_date and
            self.discontinued_date < date.today() or
            False)

    class Meta:
        """Meta data."""

        ordering = ('-discontinued_date', '-stock', 'name', 'price',)
