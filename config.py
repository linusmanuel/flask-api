from app import app

app.config.from_object('config')
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/api_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
