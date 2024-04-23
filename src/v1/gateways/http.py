from fastapi import APIRouter,  status
from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str

AppRoute = APIRouter(prefix="/v1")

@AppRoute.post("/user")
def create_user(user: User):
    return "",status.HTTP_201_CREATED

@AppRoute.delete("/user/{username}")
def delete_user(username: str):
    return "", status.HTTP_204_NO_CONTENT

@AppRoute.post("/testcase/{id}")
def run_testcase(id: int):
    return "", status.HTTP_201_CREATED
