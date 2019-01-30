"""URL Configuration."""
from django.conf.urls import url, include
from rest_framework import routers
from ecommerce import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'invoicelines', views.InvoiceViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]
