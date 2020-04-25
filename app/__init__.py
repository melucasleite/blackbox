# encoding=utf-8
import flask
import flask_sqlalchemy
import flask_migrate
import logging
from flask import Flask

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app.models import *
from app.routes import *
