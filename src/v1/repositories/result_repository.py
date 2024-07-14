from sqlalchemy.orm import Session, lazyload
from sqlalchemy.sql import func
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
    
    def reportGetlist(self, start_date, finish_date):
        data = self.db.query(Result).where(Result.execute_date.between(start_date, finish_date)).order_by(Result.execute_date.desc()).limit(5).all()

        return data
    
    def totalEfectiveness(self):
        query = self.db.query(
            (
                (func.sum(Result.test_count) - func.sum(Result.success_count)) / func.sum(Result.test_count) * 100
            ).label("total_effectiveness")
        ).where(Result.execute_date.between(self.first_day_month, self.formated_current)).first()

        total_effectiveness = query.total_effectiveness if query else 0
        
        return total_effectiveness
    
    def tag_report_list(self, start_date, finish_date):
        query = self.db.query(
            ResultTags.id,
            ResultTags.tag_name,
            func.sum(func.distinct(Result.test_count)).label('total_test'),
            func.sum(func.distinct(Result.test_count - Result.success_count)).label('failed')
        ).join(Result, ResultTags.result_id == Result.id).where(Result.execute_date.between(start_date, finish_date)).group_by(ResultTags.tag_id).order_by(func.sum(func.distinct(Result.test_count - Result.success_count)).desc()).limit(5).all()

        return query
    
    def get(self, filter = None, keyword = None, limit = 10, offset = 0):
        query = self.db.query(Result)

        if filter is not None and len(filter) != 0 and filter == "name":
            query = query.where(Result.name.like(f"{keyword}%"))
        if filter is not None and len(filter) != 0 and filter == "status":
            query = query.where(Result.test_status.like(f"{keyword}%"))
        if filter is not None and len(filter) != 0 and filter == "executor":
            query = query.where(Result.executor.like(f"{keyword}%"))
        if filter is not None and len(filter) != 0 and filter == "date" or filter == "date execute":
            query = query.where(Result.execute_date.like(f"{keyword}%"))
        if filter is not None and len(filter) != 0 and filter == "tags" or filter == "tag":
            query = query.join(ResultTags).filter(ResultTags.tag_name.like(f"{keyword}%"))

        return {
            "total_count" : query.count(),
            "data" : query.order_by(Result.execute_date.desc()).limit(limit).offset(limit*offset).all()
        } 
    
    def get_detail(self, id):
        return self.db.query(Result).where(Result.id == id).first()
    
    def delete_all(self):
        self.delete_all_tags()
        self.delete_all_messages()
        return self.db.query(Result).delete()

    def delete_all_tags(self):
        return self.db.query(ResultTags).delete()
    
    def delete_all_messages(self):
        return self.db.query(ResultMessage).delete()