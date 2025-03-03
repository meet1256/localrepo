from .database import Base
from sqlalchemy import TIMESTAMP , Column, Integer, String,Boolean,Time,Float, ForeignKey, Table , DateTime
from pydoc import text
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    firstname = Column(String,nullable=False)
    lastname = Column(String,unique=True,nullable=False)
    phone_number = Column(String,unique=True,nullable=False)
    email_id = Column(String,unique=True,nullable=False)
    hashed_password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default= text('now()'))


class Sales_Tracker(Base):
    __tablename__ = "sales"
    id= Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    url = Column(String,nullable=False)
    currency = Column(String,nullable=False)
    notification= Column(Boolean,nullable=False)
