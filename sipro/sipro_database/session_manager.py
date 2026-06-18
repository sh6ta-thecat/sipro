from contextlib import contextmanager

from sipro_database.database import SessionLocal


@contextmanager
def get_session():

    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()