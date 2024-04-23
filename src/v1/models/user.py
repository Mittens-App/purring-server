from sqlalchemy import Column, Integer, String
from config.database import EntityMeta

class User(EntityMeta):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, index=True, )
    password = Column(String(100))
    type = Column(String(1), default="1")
