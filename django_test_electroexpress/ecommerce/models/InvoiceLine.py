"""Model Class."""
from django.db import models
from ecommerce.models import Invoice
from ecommerce.models import Product
from django.db.models import Q


class InvoiceLine(models.Model):
    """InvoiceLine."""

    # TODO BORRAR
    def limit_choices_to_product():
        """Limit of eligible products per stock and discontinued date."""
        return Q(stock__gt=0)

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE)

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to=Q(stock__gt=0))

    quantity = models.IntegerField(
        default=1)

    # Unitary price of the product
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0)

    @property
    def total(self):
        """Total of all products."""
        return (self.quantity or 0) * self.price

    def save(self, *args, **kwargs):
        """Persist price on N:M model."""
        self.price = self.product and self.product.price or 0
        super().save(*args, **kwargs)
