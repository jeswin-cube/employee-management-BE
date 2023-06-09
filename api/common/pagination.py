from base64 import b64decode, b64encode
from urllib import parse


class Cursor:
    def __init__(self, datetime=None, reverse=None):
        self.datetime = datetime
        self.reverse = reverse

    def __str__(self):
        return f"datetime={self.datetime}, reverse={self.reverse}"

    def encode(self):
        if self.datetime is None:
            return None
        tokens = {
            "datetime": self.datetime,
            "reverse": self.reverse,
        }
        querystring = parse.urlencode(tokens, doseq=True)
        return b64encode(querystring.encode("ascii")).decode("ascii")

    @classmethod
    def decode(cls, cursor):
        if cursor is None:
            return None
        querystring = b64decode(cursor.encode("ascii")).decode("ascii")
        tokens = parse.parse_qs(querystring, keep_blank_values=True)
        return cls(tokens["datetime"][0], tokens["reverse"][0] == "True")
