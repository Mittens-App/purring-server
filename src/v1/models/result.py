from sqlalchemy import Column, Integer, String, Text, DATETIME, Enum, DECIMAL
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
    effectiveness = Column(DECIMAL(2,4))
    executor = Column(String(50))
    test_count = Column(Integer)
    success_count = Column(Integer)

class ResultMessage(EntityMeta):
    __tablename__ = "result_message"

    id = Column(Integer, primary_key=True)
    result_id = Column(Integer, index=True)
    result_type = Column(String(20))
    result_method = Column(String(100))
    message = Column(String(1000))

class ResultTags(EntityMeta):
    __tablename__ = "result_tags"

    id = Column(Integer, primary_key=True)
    result_id = Column(Integer, index=True)
    tag_id = Column(Integer)
    tag_name = Column(String(50), index=True)
    tag_color = Column(String(10))