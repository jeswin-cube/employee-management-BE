import jwt

from config.settings import DATA_SECRET


class JWT:
    def __init__(self, secret=None):
        if secret:
            self.secret = secret
        else:
            self.secret = DATA_SECRET
        self.algorithm = "HS256"

    def encode_data(self, data):
        return jwt.encode(data, self.secret, algorithm=self.algorithm)

    def decode_data(self, data):
        return jwt.decode(data, self.secret, algorithms=self.algorithm)
