# models.py
from sqlalchemy import Column, TEXT, INT, BIGINT, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Diary(Base):
    __tablename__ = "diary"

    id = Column(INT, primary_key=True, autoincrement=True)
    title = Column(TEXT, nullable=False)
    content = Column(TEXT, nullable=False)
    create_date = Column(DATETIME, nullable=False, default=datetime.utcnow)


class Calendar(Base):
    __tablename__ = "calendar"

    id = Column(INT, primary_key=True, autoincrement=True)
    event_name = Column(TEXT, nullable=False)
    event_date = Column(DATETIME, nullable=False)
