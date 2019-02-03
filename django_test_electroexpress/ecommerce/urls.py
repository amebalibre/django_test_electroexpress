"""URL Configuration."""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ecommerce.views import DesiredView
from ecommerce.views import ProductView
from ecommerce.views import InvoiceView
# from ecommerce.views import UserView

urlpatterns = [
    path('desireds/', DesiredView.DesiredList.as_view()),
    path('desireds/<int:pk>/', DesiredView.DesiredDetail.as_view()),
    path('desireds/<int:pk>/put/', DesiredView.DesiredPut.as_view()),
    path('desireds/add/', DesiredView.DesiredCreate.as_view()),
    path('products/', ProductView.ProductList.as_view()),
    path('products/<int:pk>/', ProductView.ProductDetail.as_view()),
    path('invoices/', InvoiceView.InvoiceList.as_view()),
    path('invoices/<int:pk>/', InvoiceView.InvoiceDetail.as_view()),
    path('invoices/add/', InvoiceView.InvoiceCreate.as_view()),
    # path('users/', UserView.UserList.as_view()),
    # path('users/<int:pk>/', UserView.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
