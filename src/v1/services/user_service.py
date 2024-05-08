from fastapi import Depends, status as http_status
from grpc import StatusCode as rpc_status
from src.v1.gateways.response import Response
from src.v1.repositories.user_repository import UserRepository
from src.v1.models.user import User
# from src.v1.gateways.http_auth import Result
from src.v1.services.auth import JwtGenerator
from sqlalchemy.exc import SQLAlchemyError
from hashlib import sha256

class UserService:
    userRepo: UserRepository
    
    def __init__(self):
        self.userRepo = UserRepository()
    
    def create(self, payload):
        user = User()
        user.password = sha256(payload.password.encode()).hexdigest()
        user.username = payload.name

        result = Response(
            body="success",
            status=http_status.HTTP_201_CREATED
        )
        try:
            self.userRepo.create(user)
            self.userRepo.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__)
            self.userRepo.rollback()
            # logging here
            result.body = error
            result.status= http_status.HTTP_500_INTERNAL_SERVER_ERROR

        return result

    def delete(self, username):
        result = 0
        try:
            result = self.userRepo.delete_by_name(username)
            self.userRepo.commit()
        except SQLAlchemyError as e:
            self.userRepo.rollback()
            error = str(e.__dict__)

        return result
    
    def exist(self, username, password):
        user = User()
        user.password = sha256(password.encode()).hexdigest()
        user.username = username
        return self.userRepo.get(user) is not None

    def get(self, username, password):
        user = User()
        user.password = sha256(password.encode()).hexdigest()
        user.username = username
        return self.userRepo.get(user)

    def login(self, username, password):
        user: User = self.get(
            username=username,
            password=password
        )
        result = Response(
            body={
                'id': 0,
                'username': None,
                'token': None,
            },
            status=rpc_status.OK
        )
        if user is None:
            result.status = rpc_status.NOT_FOUND
            return result
        
        result.body['id'] = user.id
        result.body['status'] = "OK"
        result.body['username'] = user.username
        generator = JwtGenerator()

        token = generator.encode(result.body)
        result.body['token'] = token

        return result