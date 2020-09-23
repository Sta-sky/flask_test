from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)

class Config(object):
    pass

class Devconfig(object):
    # SQLALCHEMY_DATABASE_URL = 'mysql+pymsql://username:passwd@host:port/dbname'
    # SQLALCHEMT_TRACK_MODIFICATIONS = False
    pass
    
    

