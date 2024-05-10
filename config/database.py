from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.loader import ConfigLoad as cfg

# Generate Database URL
DATABASE_URL = f"{cfg['db']['dialect']}://{cfg['db']['username']}:{cfg['db']['password']}@{cfg['db']['host']}:{cfg['db']['port']}/{cfg['db']['database']}"
ISOLATION_LEVEL = "READ COMMITTED"
if cfg['db']['dialect'] == "sqlite":
    DATABASE_URL = "sqlite:///./purring.db"
    ISOLATION_LEVEL = "READ UNCOMMITTED"

# Create Database Engine
Engine = create_engine(
    DATABASE_URL, echo=cfg['db']['debug'], future=True, isolation_level=ISOLATION_LEVEL
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