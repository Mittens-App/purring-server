from sqlalchemy.orm import Session, lazyload
from config.database import db_connection
from src.v1.models.result import Result, ResultMessage, ResultTags

class ResultRepository:
    db: Session

    def __init__(
        self, db: Session = next(db_connection())
    ) -> None:
        self.db = db

    def commit(self):
        self.db.commit()
    
    def rollback(self):
        self.db.rollback()
    
    def create(self, result: Result):
        self.db.add(result)
        self.db.flush()
        return result

    def createTags(self, tags = []):
        self.db.add_all(tags)

    def createMessage(self, msg = []):
        self.db.add_all(msg)