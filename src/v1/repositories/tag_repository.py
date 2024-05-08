from sqlalchemy.orm import Session
from config.database import db_connection
from src.v1.models.tag import Tag

class TagRepository:
    db: Session

    def __init__(
        self, db: Session = next(db_connection())
    ) -> None:
        self.db = db

    def commit(self):
        self.db.commit()
    
    def rollback(self):
        self.db.rollback()
    
    def create(self, tag: Tag):
        self.db.add(tag)
    
    def get(self, keyword):
        query = self.db.query(Tag)

        if keyword is not None and len(keyword) != 0:
            query = query.where(Tag.name.like(f"{keyword}%"))

        return query.order_by(Tag.name.asc()).all()
    
    def get_by_id(self, id):
        return self.db.query(Tag).where(Tag.id==id).first()
    
    def delete_by_id(self, id):
        return self.db.query(Tag).where(Tag.id==id).delete()