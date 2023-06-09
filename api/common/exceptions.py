import json

class OtpNotSentException(Exception):
    pass


class HttpClientErrorException(Exception):
    def __init__(self, response):
        self.value = {
            "message": json.loads(response.content)
            if response.content
            else "Something went wrong",
            "status": response.status_code,
        }

    def __dict__(self):
        return self.value

    def __str__(self):
        """
        Define the __str__ method in case we want to serialize the exception.

        Returns:
            Serializable representation
        """
        return repr(self.value)
