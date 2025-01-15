from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)
    username = Column(String, primary_key=False)
    password = Column(String, primary_key=False)

class Interests(Base):
    __tablename__ = 'Interests'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)
    Activities = Column(String, primary_key=False)
    Groups = Column(String, primary_key=False)
    Languages = Column(String, primary_key=False)
    Budget_range = Column(String, primary_key=False)
    Distance_range = Column(String, primary_key=False)

