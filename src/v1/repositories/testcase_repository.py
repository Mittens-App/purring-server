from sqlalchemy.orm import Session, lazyload
from sqlalchemy import Row, func
from config.database import db_connection
from src.v1.models.testcase import TestCase,TestCaseTags
from src.v1.models.tag import Tag

class TestcaseRepository:
    db: Session

    def __init__(
        self, db: Session = next(db_connection())
    ) -> None:
        self.db = db

    def commit(self):
        self.db.commit()
    
    def rollback(self):
        self.db.rollback()
    
    def create(self, testcase: TestCase):
        self.db.add(testcase)
    
    def get(self, id: int):
        return self.db.query(TestCase).where(TestCase.id==id).first()
    
    def getWithTags(self, id: int):
        return self.db.query(TestCase, TestCaseTags, Tag).join(
                TestCaseTags, 
                TestCase.id==TestCaseTags.testcase_id,
                isouter=True
            ).join(
                Tag,
                TestCaseTags.tag_id==Tag.id,
                isouter=True
            ).where(TestCase.id==id).all()

    def getAll(self, filter=None, keyword=None, limit=25, offset=0):
        query = self.db.query(TestCase).join(
                TestCaseTags, 
                TestCase.id==TestCaseTags.testcase_id,
                isouter=True
            ).join(
                Tag,
                TestCaseTags.tag_id==Tag.id,
                isouter=True
            )
        if filter is not None and len(filter) != 0:
            query.where(TestCase.name.like(f"{keyword}%"))
        
        query.group_by(TestCase.id)
        return {
            "total_count": query.count(),
            "data" : query.order_by(TestCase.name).limit(limit).offset(limit*offset).all()
            }