"""Custom Exceptions."""
from rest_framework.exceptions import APIException
from rest_framework import status


class NotAcceptableOnInvoiceModel(APIException):
    """The invoice can't be updated because it has already been paid."""

    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_code = 'unauthorized'
    default_detail = \
        "Invoice can't be updated beause it has already been paid!"


class ServerErrorOnCreate(APIException):
    """Isn't possible create for some problem."""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = 'internal_server_error'
    default_detail = "Isn't possible create it for some problem."