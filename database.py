from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://utsavsharma:1969@localhost/medical_guidelines"

# Create a synchronous engine
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

# Dependency function for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
