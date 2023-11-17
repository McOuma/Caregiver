from __init__ import Base, engine
from sqlalchemy import Column, Integer, ForeignKey, String

class Care_Giver(Base):
    __tablename__="care_givers"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(25), nullable=False, unique=True)
    gender = Column(String(255), nullable=False,unique=True)
    age = Column(Integer, nullable=False)

    

Base.metadata.create_all(engine)