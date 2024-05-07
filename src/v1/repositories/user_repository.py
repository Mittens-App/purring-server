from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from config.database import db_connection
from src.v1.models.user import User

class UserRepository:
    db: Session

    def __init__(
        self, db: Session = next(db_connection())
    ) -> None:
        self.db = db

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def create(self, user: User):
        self.db.add(user)
    
    def get_by_name(self, username) -> User:
        return self.db.query(User).where(User.username==username).first()
    
    def get(self, user: User):
        return self.db.query(User).where(User.username==user.username, User.password==user.password).first()
    
    def delete_by_name(self, username):
        return self.db.query(User).where(User.username==username).delete()