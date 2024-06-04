from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from django.http import JsonResponse


def error404_hadler(request, *args, **kwargs):
    return JsonResponse(
        {
            "detail": "Not found",
            "status_code": 404
        }, 
        status=404
    )


def drf_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if issubclass(type(exc), APIException):
        response_data = {
            'status_code': exc.status_code,
            'code': exc.default_code,
            'detail': exc.detail
        }
        response.data = response_data
    return response