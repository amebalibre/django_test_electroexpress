"""Custom Exceptions."""
from rest_framework.exceptions import APIException
from rest_framework import status


class NotAcceptableOnInvoiceModel(APIException):
    """The invoice can't be modified because it has already been paid."""

    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_code = 'unauthorized'
    default_detail = \
        "Invoice can't be create/destroy beause it has already been paid!"
class NotAcceptableOnPromoModel(APIException):
    """The promo can't be modified because it has already been paid."""

    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_code = 'not_acceptable_on_promos'
    default_detail = "The promotion can not be modified / destroyed " \
                     "because there are invoices charged!"


class ServerErrorOnCreate(APIException):
    """Isn't possible create for some problem."""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = 'internal_server_error'
    default_detail = "Isn't possible create it for some problem."
