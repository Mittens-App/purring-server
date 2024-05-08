from sqlalchemy import Column, Integer, String, DATETIME, Enum, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from config.database import EntityMeta
import enum

class StatusEnum(enum.Enum):
    success = "success"
    failed = "failed"
    running = "running"

class Mittens(EntityMeta):
    __tablename__ = "mittens"

    id = Column(Integer, primary_key=True)
    execute_date = Column(DATETIME, index=True)
    duration = Column(Integer)
    test_status = Column(Enum(StatusEnum))
    effectiveness = Column(DECIMAL(2,4))
    executor = Column(String(50))
    test_count = Column(Integer)
    # 1 to many relation
    messages = relationship("MittensMessage", backref=__tablename__)
    # 1 to many relation
    tags = relationship("MittensTags", backref=__tablename__)

class MittensMessage(EntityMeta):
    __tablename__ = "mittens_message"

    id = Column(Integer, primary_key=True)
    mittens_id = Column(Integer, ForeignKey("mittens.id"))
    result_type = Column(String(20))
    result_method = Column(String(100))
    message = Column(String(1000))

class MittensTags(EntityMeta):
    __tablename__ = "mittens_tags"

    id = Column(Integer, primary_key=True)
    mittens_id = Column(Integer, ForeignKey("mittens.id"))
    tag_name = Column(String(50), index=True)
    tag_color = Column(String(10))