from sqlalchemy import Column, Integer, String, Text, DATETIME, Enum, ForeignKey
from sqlalchemy.orm import relationship
from config.database import EntityMeta
import enum

class ResultEnum(enum.Enum):
    success = "success"
    failed = "failed"
    empty= ""

class TestCase(EntityMeta):
    __tablename__ = "testcase"

    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, index=True)
    description = Column(Text)
    file = Column(Text)
    creator = Column(String(50))
    last_execute_date = Column(DATETIME)
    last_result = Column(Enum(ResultEnum))
    # 1 to many relation
    testcase_tags = relationship("TestCaseTags", backref=__tablename__)

class TestCaseTags(EntityMeta):
    __tablename__ = "testcase_tags"

    id = Column(Integer, primary_key=True)
    testcase_id = Column(Integer, ForeignKey("testcase.id"))
    tag_id = Column(Integer, ForeignKey("tag.id"))
    # 1 on 1 relation
    tag = relationship("Tag", uselist=False)
