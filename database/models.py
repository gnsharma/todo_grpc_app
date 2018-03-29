from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root@localhost/todo', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)

    def __str__(self):
        return self.name

    todo = relationship("Todo", cascade="all, delete-orphan")


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    details = Column(String(256), nullable=False)
    status = Column(Integer, nullable=False)

    def __str__(self):
        return self.details
    

