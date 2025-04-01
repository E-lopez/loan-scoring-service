import os

basedir = os.path.abspath(os.path.dirname(__file__))

username = 'root'
password = '%40r00t$usR'
userpass = 'mysql+mysqldb://' + username + ':' + password + '@'
server = 'localhost:3306'
dbname = '/user_scores'

class Config:
# create and configure the app
  SQLALCHEMY_DATABASE_URI = userpass + server + dbname
  SECRET_KEY = os.environ.get('SECRET_KEY')
  # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
  #     or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

