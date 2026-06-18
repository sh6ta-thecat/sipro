from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sipro_core.settings import Settings

DATABASE_URL = f"sqlite:///{Settings.DATABASE_FILE}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
