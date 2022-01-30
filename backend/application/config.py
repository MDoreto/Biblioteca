from os import environ 
from datetime import timedelta
class Config(object):
    DEBUG = False

    SECRET_KEY = environ.get('SECRET_KEY')

    user = environ.get('DB_USER')
    password = environ.get('DB_PASS')
    host = environ.get('DB_HOST')
    database = environ.get('DB_DB')
    port = environ.get('DB_PORT')
    
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

    JWT_TOKEN_LOCATION= ["cookies"]

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_COOKIE_SECURE = False
