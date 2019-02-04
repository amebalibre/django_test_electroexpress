"""Very bad test class.

El apartado de testing lo he descuidado demasiado pensando constantemente
en obtener un MVP operativo dentro de un límite de tiempo razonable ya que
no dispongo del tiempo que quisiera para trabajar en la prueba.

No es que no valore el testing, es sencillamente que debía aprender algunos
conceptos de DRF que me impedían poder realizar un desarrollo ágil y eficiente.
"""
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

from ecommerce.views import InvoiceView


class InvoiceTests(TestCase):
    """Invoice testing."""

    def setUp(self):
        """Set up the data."""
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='anyuser', email='anyuser@mail.com', password='1234')

    def test_list(self):
        """Test invoice list andd user access."""
        # Create an instance of a GET request.
        request = self.factory.get('/ecommerce/invoices')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = InvoiceView(request)
        # Use this syntax for class-based views.
        response = InvoiceView.as_view()(request)
        self.assertEqual(response.status_code, 200)
