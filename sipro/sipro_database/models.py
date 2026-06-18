from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    BigInteger,
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Installation(Base):

    __tablename__ = "installations"

    id = Column(Integer, primary_key=True)

    username = Column(String(100))

    computer_name = Column(String(100))

    filename = Column(String(255))

    full_path = Column(String(500))

    sha256 = Column(String(64))

    status = Column(String(50))

    start_time = Column(DateTime)

    end_time = Column(DateTime)

    duration_seconds = Column(Integer)

    exit_code = Column(Integer)

    file_size = Column(BigInteger)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(
        String(100),
        unique=True,
    )

    total_installations = Column(Integer, default=0)

    successful_installations = Column(Integer, default=0)

    failed_installations = Column(Integer, default=0)
