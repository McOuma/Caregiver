from __init__ import Base, engine
from sqlalchemy import Column, Integer, ForeignKey, String
from user import User

class Client(User):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(80), nullable=False, unique=True)
    gender = Column(String(10), nullable=False, unique=True)
    


Base.metadata.create_all(engine)