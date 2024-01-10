from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    name = Column(String)
    email = Column(String)
    password = Column(String)
