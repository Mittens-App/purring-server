from config.loader import ApiKey
from datetime import datetime, timedelta
import jwt

class JwtGenerator():
    __alg: str
    __secret: str
    __lifetime: int

    def __init__(self):
        self.__alg = "HS256"
        self.__secret = ApiKey
        self.__lifetime = 3

    def encode(self, payload) -> str:
        payload['expr'] = (datetime.now() + timedelta(days=self.__lifetime)).timestamp()
        return jwt.encode(payload=payload, key=self.__secret, algorithm=self.__alg)
    
    def decode(self, raw_token):
        token = raw_token.split("Bearer ")[1]
        return jwt.decode(jwt=token, key=self.__secret, algorithms=[self.__alg])