from flask import Flask
from sqlalchemy.orm import sessionmaker
from model import User,Accounts,Care_Giver,Client,Admin,Sub_admin,engine

Session = sessionmaker(bind=engine)
session =Session()

app = Flask(__name__)


@app.route('/user', method =["POST", "GET"])
def create_user(user):
   # if user = None
   return
    

if __name__=="__main__":
    app(debug =True)