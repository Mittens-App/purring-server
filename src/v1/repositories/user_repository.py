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

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return ''
    
    def get(self, username) -> User:
        return self.db.get(
            User, {
                User.username.name, username
            }
        )
    
    def delete(self, id):
        user = self.db.session.get(User, id)
        self.db.delete(user)
        self.db.commit()