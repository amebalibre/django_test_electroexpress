"""URL Configuration."""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ecommerce.views import ProductView
from ecommerce.views import InvoiceView

urlpatterns = [
    path('products/', ProductView.ProductList.as_view()),
    path('products/<int:pk>/', ProductView.ProductDetail.as_view()),
    path('invoices/', InvoiceView.InvoiceList.as_view()),
    path('invoices/<int:pk>/', InvoiceView.InvoiceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
