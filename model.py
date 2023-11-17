from sqlalchemy import create_engine,ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship
from sqlalchemy.ext.declarative import declarative_base

database_uri  = "sqlite:///caregiver.db"
engine = create_engine(database_uri)
Model = declarative_base()


class User(Model):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_name = Column(String(25), nullable=False, unique=True)
    full_name = Column(String(255), nullable=False,unique=True)
    password = Column(String(80), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)

class Client(Model):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(80), nullable=False, unique=True)
    gender = Column(String(10), nullable=False, unique=True)


class Care_Giver(Model):
    __tablename__="care_givers"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(25), nullable=False, unique=True)
    gender = Column(String(255), nullable=False,unique=True)
    age = Column(Integer, nullable=False)


class Admin(Model):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(80), nullable=False, unique=True)
    department = Column(String(25), nullable=False, unique=True)


class Accounts(Model):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(25), nullable=False, unique=True)
    gender = Column(String(10), nullable=False,unique=True)


class Sub_admin(Model):
    __tablename__ = "sub_admins"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(25), nullable=False, unique=True)
    gender = Column(String(10), nullable=False,unique=True)


Model.metadata.create_all(engine)




