from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, Date

import datetime

Base = declarative_base()

class WHO_Guideline(Base):
    __tablename__ = "guidelines"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    date = Column(Date, nullable=False) 
    link = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<WHO_Guideline(id={self.id}, title={self.title})>"

# New Document model for storing medical documents and summaries
class Document(Base):
    __tablename__ = 'documents'  

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    summary = Column(Text, nullable=False) 

    def __repr__(self):
        return f"<Document(id={self.id}, title={self.title})>"