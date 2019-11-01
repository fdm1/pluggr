from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime


class Thing(Base):
    """
    Example Signups table
    """

    __tablename__ = "things"
    id = Column(Integer, primary_key=True)
    value = Column(String(256))
    created_timestamp = Column(DateTime())
