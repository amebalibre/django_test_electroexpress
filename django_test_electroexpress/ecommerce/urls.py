"""URL Configuration."""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ecommerce.views import DesiredView
from ecommerce.views import InvoiceView
from ecommerce.views import ProductView
from ecommerce.views import PromoView

urlpatterns = [
    # desireds
    path('desireds/', DesiredView.DesiredList.as_view()),
    path('desireds/<int:pk>/', DesiredView.DesiredDetail.as_view()),
    # products
    path('products/', ProductView.ProductList.as_view()),
    path('products/<int:pk>/', ProductView.ProductDetail.as_view()),
    # invoices
    path('invoices/', InvoiceView.InvoiceList.as_view()),
    path('invoices/<int:pk>/', InvoiceView.InvoiceDetail.as_view()),
    # promos
    path('promos/', PromoView.PromoList.as_view()),
    path('promos/<int:pk>/', PromoView.PromoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
