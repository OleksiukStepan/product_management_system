from sqlalchemy.orm import Session

from src.database import SessionLocal


async def get_db() -> Session:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
