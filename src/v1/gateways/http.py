from fastapi import APIRouter, status, Depends, Response, BackgroundTasks
from pydantic import BaseModel
from typing import Annotated
from src.v1.gateways.http_auth import basic_auth, api_key_auth
from src.v1.services.user_service import UserService
from src.v1.services.testcase_service import TestcaseService

AppRoute = APIRouter(prefix="/v1", )

class User(BaseModel):
    name: str
    password: str

@AppRoute.post("/user")
def create_user(user: User, response: Response, credentials = Depends(api_key_auth), userService: UserService = Depends()):
    result = userService.create(
        payload=user
    )
    response.status_code = result.status
    return result.body

@AppRoute.delete("/user/{username}")
def delete_user(username: str, response: Response, credentials = Depends(api_key_auth), userService: UserService = Depends()):
    userService.delete(username)
    response.status_code = status.HTTP_204_NO_CONTENT
    return None

@AppRoute.post("/testcase/{id}")
def run_testcase(id: int, response: Response, credentials = Depends(basic_auth), testcaseService: TestcaseService = Depends()):
    result = testcaseService.run(id, credentials.username)
    response.status_code = result.status
    return result.body
