from __init__ import Base, engine
from sqlalchemy import Column, Integer, ForeignKey, String

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_name = Column(String(25), nullable=False, unique=True)
    full_name = Column(String(255), nullable=False,unique=True)
    password = Column(String(80), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    
    def __repr__(self):
        return f"{__class__}"

Base.metadata.create_all(engine)