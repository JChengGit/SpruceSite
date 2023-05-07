from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    uname = Column(String)
    password = Column(String)
    role = Column(Integer, ForeignKey("role.id"))


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Session(Base):
    __tablename__ = "session"

    session_key = Column(String, primary_key=True)
    session_data = Column()
