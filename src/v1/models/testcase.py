from sqlalchemy import Column, Integer, String, Text, DATETIME, Enum
from config.database import EntityMeta
import enum

class ResultEnum(enum.Enum):
    success = "success"
    failed = "failed"

class TestCase(EntityMeta):
    __tablename__ = "testcase"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, index=True)
    description = Column(Text)
    file = Column(Text)
    creator = Column(String(50))
    last_execute_date = Column(DATETIME)
    last_result = Column(Enum(ResultEnum))

class TestCaseTags(EntityMeta):
    __tablename__ = "testcase_tags"

    id = Column(Integer, primary_key=True)
    testcase_id = Column(Integer, index=True)
    tag_id = Column(Integer, index=True)
