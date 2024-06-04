from rest_framework import exceptions


class ObjectAlreadyExists(exceptions.APIException):
    default_detail = "Object already exists"
    status_code = 400
    default_code = "no_duplication_allowed"


class InvalidFilterType(exceptions.APIException):
    default_detail = "Invalid filter type"
    status_code = 400
    default_code = "invalid_filter"


class InvalidPrice(exceptions.APIException):
    default_detail = "Invalid min or max price"
    status_code = 400
    default_code = "invalid_price"


class InvalidPriceNegative(exceptions.APIException):
    default_detail = "Invalid min or max price. Price cannot be negative"
    status_code = 400
    default_code = "invalid_price_negative"


class InvalidPriceMinGreaterThanMax(exceptions.APIException):
    default_detail = "Min price cannot be greater than max price"
    status_code = 400
    default_code = "invalid_price_greater"