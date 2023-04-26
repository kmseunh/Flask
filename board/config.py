import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1111@localhost:3306/shboard'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
