from fastapi import Depends
from src.v1.repositories.user_repository import UserRepository
from src.v1.models.user import User

class UserService:
    userRepo: UserRepository
    
    def __init__(self, userRepo: UserRepository = Depends()):
        self.userRepo = userRepo
    
    def create(self, payload):
        user = User()
        user.password = payload.password
        user.username = payload.name
        self.userRepo.create(user)