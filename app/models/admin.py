from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Relationship
from __init__ import Base, engine
from user import User

class Admin(User):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(80), nullable=False, unique=True)
    department = Column(String(25), nullable=False, unique=True)



Base.metadata.create_all(engine)



