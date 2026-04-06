import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config :
   
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Mamba-one'
    SQLALCHEMY_DATABASE_URI = os.eniron.get("DATABASE_URL") or 'sqlite:///' + os.path.join(basedir,'app.db')
    