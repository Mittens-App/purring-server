from fastapi import Depends, status as http_status
from src.v1.repositories.user_repository import UserRepository
from src.v1.models.user import User
from src.v1.gateways.http_auth import Result
from sqlalchemy.exc import SQLAlchemyError
from hashlib import sha256

class UserService:
    userRepo: UserRepository
    
    def __init__(self, userRepo: UserRepository = Depends()):
        self.userRepo = userRepo
    
    def create(self, payload):
        user = User()
        user.password = sha256(payload.password.encode()).hexdigest()
        user.username = payload.name

        result = Result(
            body="success",
            status=http_status.HTTP_201_CREATED
        )
        try:
            self.userRepo.create(user)
            self.userRepo.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            # logging here
            result.body = error
            result.status= http_status.HTTP_500_INTERNAL_SERVER_ERROR

        return result

    def delete(self, username):
        user = self.userRepo.get_by_name(username=username)
        print(user)
    
    def exist(self, username, password):
        user = User()
        user.password = password
        user.username = username
        return self.userRepo.get(user) is not None