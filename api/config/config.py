import os
from decouple import config
from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

db_name = 'pizza_db'


default_uri = "postgres://{}:{}@{}/{}".format('postgres', 'password', 'localhost:5432', db_name)
uri = config("DATABASE_URL", default_uri)  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`


class Config:
    SECRET_KEY = config('SECRET_KEY', 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True
    DEBUG=True

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=uri
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG=config('DEBUG', False, cast=bool)


config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}