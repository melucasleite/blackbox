import os
from dotenv import load_dotenv

load_dotenv()
DEBUG = False
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", 'mysql+pymysql://root:root@localhost:3306/blackbox')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'blackbox'
