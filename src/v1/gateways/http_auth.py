from fastapi import status, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials, APIKeyHeader
from typing import Annotated

class Result(object):
    def __init__(self, body, status):
        self.body = body
        self.status = status

security = HTTPBasic()
X_API_KEY = APIKeyHeader(name='X-API-Key')

def api_key_auth(x_api_key: str = Depends(X_API_KEY)):
    from config.loader import api_key

    if x_api_key != api_key():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    return True


from src.v1.services.user_service import UserService
def basic_auth(credentials: Annotated[HTTPBasicCredentials, Depends(security)], userService: UserService = Depends()):
    isAuthorize = userService.exist(
        username=credentials.username,
        password=credentials.password
    )
    
    if isAuthorize is False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials
