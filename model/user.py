from sqlalchemy import Column, ForeignKey, Integer, String

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey("role.id"))


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Session(Base):
    __tablename__ = "session"

    session_key = Column(String, primary_key=True)
    user_id = Column(Integer)
    user_name = Column(String)
    create_time = Column(Integer)
