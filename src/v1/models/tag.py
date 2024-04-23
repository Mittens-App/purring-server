from sqlalchemy import Column, Integer, String, Text
from config.database import EntityMeta

class Tag(EntityMeta):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, index=True, )
    description = Column(Text)
    color = Column(String(10))