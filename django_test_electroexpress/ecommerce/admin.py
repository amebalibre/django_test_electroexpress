"""Admin class."""
from django.contrib import admin
from ecommerce.models import Product
from ecommerce.models import Promo
from ecommerce.models import Invoice
from ecommerce.models import InvoiceLine


class ProductAdmin(admin.ModelAdmin):
    """View for product Admin."""

    list_display = ['name', 'price', 'type', 'stock', 'discontinued_date']
    fieldsets = [
        ('Product', {'fields': [
            'name',
            'price',
            'type',
        ]}),
        ('Meta', {'fields': [
            'stock',
            'inclusion_date',
            'discontinued_date',
        ]})
    ]


class PromoAdmin(admin.ModelAdmin):
    """View for promo Admin."""

    list_display = ['code', 'type', 'value', 'active']
    fieldsets = [
        ('Promo', {'fields': [
            'code',
            'type',
            'value',
            'active',
        ]}),
    ]


class InvoiceLineInLine(admin.TabularInline):
    """Lines on tabular mode."""

    model = InvoiceLine
    extra = 1


class InvoiceAdmin(admin.ModelAdmin):
    """Admin portal."""

    list_display = [
        'payment_date',
        'total_lines',
        'total_promos',
        'shipping_cost',
        'total',
    ]

    fieldsets = [
        ('Invoice',
            {'fields': [
                'promos',
                'shipping_cost',
                'payment_date',
            ]}),
        ]

    inlines = [InvoiceLineInLine]


admin.site.register(Product, ProductAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(Invoice, InvoiceAdmin)
