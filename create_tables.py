from sqlalchemy import create_engine
from models import Base

DATABASE_URL = "postgresql://utsavsharma:1969@localhost/medical_guidelines"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)
