from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from config.database import db_connection
from src.v1.models.user import User

class UserRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(db_connection)
    ) -> None:
        self.db = db

    def commit(self):
        self.db.commit()

    def create(self, user: User):
        self.db.add(user)
    
    def get_by_name(self, username) -> User:
        return self.db.query(User).all()
    
    def get(self, user: User):
        return self.db.query(User).where(User.username==user.username, User.password==user.password).first()
    
    def delete(self, id):
        user = self.db.query(User, id)
        self.db.delete(user)
        self.db.commit()