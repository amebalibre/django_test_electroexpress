"""Model Class."""
from django.db import models
from django.db import transaction
from ecommerce.models import Promo
from decimal import Decimal
from decimal import ROUND_DOWN
from decimal import ROUND_UP
from datetime import date
from sequences import get_next_value
_UNNAMED = 'New Invoice'  # default name when sequence generate


class Invoice(models.Model):
    """Purchase made by the customer.

    If you don't have payment_date, then it's considered a shopping cart.
    """

    IN_SPAIN = Decimal.from_float(6.0).quantize(
        Decimal('.01'), rounding=ROUND_UP)
    OUT_SPAIN = Decimal.from_float(15.45).quantize(
        Decimal('.01'), rounding=ROUND_UP)
    SHIPPING_COST_CHOICES = (
        (IN_SPAIN, 'Shipping to spain ({}€)'.format(IN_SPAIN)),
        (OUT_SPAIN, 'International ({}€)'.format(OUT_SPAIN)))

    name = models.CharField(
        max_length=15,  # That's +2 length for unexpected
        default=_UNNAMED)

    # user
    promos = models.ManyToManyField(
        to='Promo',
        null=True,
        blank=True)

    shipping_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        choices=SHIPPING_COST_CHOICES,
        default=IN_SPAIN,
        blank=True)

    payment_date = models.DateField(
        default=date.today()
    )

    lines = models.ManyToManyField(
        to='Product',
        through='InvoiceLine',
        through_fields=('invoice', 'product'))

    @property
    def total_promos(self):
        """Calculate the total promotion depending on type of promotion."""
        total = 0
        for promo in self.promos.all():
            if(promo.active):
                if(promo.type == Promo.PERCENT):
                    percent = Decimal.from_float(promo.value / 100).quantize(
                        Decimal('.01'), rounding=ROUND_DOWN)  # only 2 decimals
                    total += self.total_lines * percent
                elif(promo.type == Promo.COMPLETE):
                    total += promo.value
                else:
                    raise NameError(
                        '{} is not defined! Check Promo.TYPE_CHOICES'.format(
                            promo.type))
        return total

    @property
    def total_lines(self):
        """Price of all invoicelines."""
        return sum(
            [t.total for t in self.invoiceline_set.all() if t.total]) or 0

    @property
    def total(self):
        """Total of all products."""
        return self.total_lines + \
            (self.shipping_cost or 0) - \
            (self.total_promos or 0)

    @transaction.atomic
    def _sequence_name(self):
        """Generate and return a sequence for name.

        This method block all transactions.
        """
        next = '{:04d}'.format(get_next_value(self.__module__))
        return '{prefix}{date}{next}'.format(
            prefix='INV',
            date=date.today().strftime('%y%m%d'),
            next=next
        )

    def __str__(self):
        """Verbose object."""
        return self.name or _UNNAMED

    def save(self, *args, **kwargs):
        """Overwrite save for autogenerated name."""
        self.name = self._sequence_name()
        super().save(*args, **kwargs)

    class Meta:
        """Meta data."""

        ordering = ('payment_date',)
