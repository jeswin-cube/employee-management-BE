import json
import urllib.parse

import requests

from .exceptions import HttpClientErrorException


class HttpClient:
    """General purpose Http Client."""

    @staticmethod
    def process_response(response):
        """
        Process the Http response.

        Args:
            response: requests.response

        Returns:
            response_data: Dict

        Raises:
            Client Error if the error code is greater than 2XX
        """
        if response.ok:
            try:
                if response.content:
                    return json.loads(response.content)
                else:
                    return {"message": "successful"}
            except Exception:
                return {
                    key: val
                    for key, val in urllib.parse.parse_qsl(response.content.decode())
                }
        else:
            raise HttpClientErrorException(response)

    @classmethod
    def get(cls, url, headers=None, params=None):
        """
        Http GET Request Handler.

        Args:
            url: string
            headers: Dict
            params: Dict

        Returns:
            response: requests.response
        """
        return requests.request("GET", url, params=params, headers=headers)

    @classmethod
    def post(
        cls, url, data=None, headers=None, params=None, files=None, json_dump=True
    ):
        """
        Http POST Request Handler.

        Args:
            url: string
            data: Dict
            headers: Dict
            params: Dict

        Returns:
            response: requests.response
        """
        if json_dump:
            return requests.request(
                "POST",
                url,
                data=json.dumps(data),
                params=params,
                headers=headers,
                files=files,
            )
        else:
            return requests.request(
                "POST",
                url,
                data=data,
                params=params,
                headers=headers,
                files=files,
            )

    @classmethod
    def put(cls, url, data=None, headers=None, params=None):
        """
        Http PUT Request Handler.

        Args:
            url: string
            data: Dict
            headers: Dict
            params: Dict

        Returns:
            response: requests.response
        """
        if isinstance(data, dict):
            return requests.request(
                "PUT", url, data=json.dumps(data), params=params, headers=headers
            )
        else:
            return requests.request(
                "PUT", url, data=data, params=params, headers=headers
            )

    @classmethod
    def delete(cls, url, headers=None, params=None):
        """
        Http POST Request Handler.

        Args:
            url: string
            headers: Dict
            params: Dict

        Returns:
            response: requests.response
        """
        return requests.request("DELETE", url, params=params, headers=headers)
