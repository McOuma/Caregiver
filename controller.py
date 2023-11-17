from sqlalchemy.orm import sessionmaker
from model import User,Accounts,Care_Giver,Client,Admin,Sub_admin,engine

Session = sessionmaker(bind=engine)
session =Session()

