from sqlalchemy import Column, Integer, String, Text, DATETIME, Enum, Double, ForeignKey
from sqlalchemy.orm import relationship
from config.database import EntityMeta
import enum

class StatusEnum(enum.Enum):
    success = "success"
    failed = "failed"
    running = "running"

class Result(EntityMeta):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    description = Column(Text)
    execute_date = Column(DATETIME, index=True)
    duration = Column(Integer)
    test_status = Column(Enum(StatusEnum))
    effectiveness = Column(Double)
    executor = Column(String(50))
    test_count = Column(Integer)
    success_count = Column(Integer)
    # 1 to many relation
    messages = relationship("ResultMessage", backref=__tablename__)
    # 1 to many relation
    tags = relationship("ResultTags", backref=__tablename__)

class ResultMessage(EntityMeta):
    __tablename__ = "result_message"

    id = Column(Integer, primary_key=True)
    result_id = Column(Integer, ForeignKey("result.id"))
    result_type = Column(String(20))
    result_method = Column(String(100))
    message = Column(String(1000))

class ResultTags(EntityMeta):
    __tablename__ = "result_tags"

    id = Column(Integer, primary_key=True)
    result_id = Column(Integer, ForeignKey("result.id"))
    tag_id = Column(Integer)
    tag_name = Column(String(50), index=True)
    tag_color = Column(String(10))