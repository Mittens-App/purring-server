from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.loader import config_load
from src.v1.models import *

# Runtime Environment Configuration
cfg = config_load()

# Generate Database URL
DATABASE_URL = f"{cfg['db']['dialect']}://{cfg['db']['username']}:{cfg['db']['password']}@{cfg['db']['host']}:{cfg['db']['port']}/{cfg['db']['database']}"
print(DATABASE_URL)
# DATABASE_URL = "sqlite:///./sql_app.db"
# DATABASE_URL = "mysql://user:password@postgresserver/db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Create Database Engine
Engine = create_engine(
    DATABASE_URL, echo=cfg['db']['debug'], future=True
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=Engine
)

def db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()

# Base Entity Model Schema
EntityMeta = declarative_base()

def init_db():
    EntityMeta.metadata.create_all(bind=Engine)