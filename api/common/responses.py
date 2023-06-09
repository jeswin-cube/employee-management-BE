import json

import pydantic
from rest_framework import status
from rest_framework.response import Response as DRFResponse

from api.common.exceptions import HttpClientErrorException


class Response:
    """generic response class."""

    @staticmethod
    def generate(status, message, data=None):
        if data:
            if not message:
                return DRFResponse(data, status=status)
            if isinstance(data, dict):
                return DRFResponse({"message": message, **data}, status=status)
            elif isinstance(data, HttpClientErrorException):
                return DRFResponse(
                    {"message": message, "reasons": [data.value]}, status=status
                )
            else:
                return DRFResponse(
                    {"message": message, **{"reasons": [repr(data)]}}, status=status
                )
        else:
            return DRFResponse({"message": message}, status=status)

    @staticmethod
    def request_data_validation_failed(error=None):
        reasons = ["Missing required parameters"]
        if isinstance(error, pydantic.ValidationError):
            reasons = json.loads(error.json())
        return Response.generate(
            status.HTTP_400_BAD_REQUEST,
            "Something went wrong",
            {"reasons": reasons},
        )

    @staticmethod
    def assertion_failed(error):
        reasons = [f"Assertion failed - {error}"]
        return Response.generate(
            status.HTTP_400_BAD_REQUEST,
            "Something went wrong",
            {"reasons": reasons},
        )
