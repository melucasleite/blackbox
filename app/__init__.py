# encoding=utf-8
import flask
import flask_sqlalchemy
import flask_migrate
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask import Response, jsonify, Flask

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app.models import *
from app.routes import *
# from app.utils import error_handlers
# from app.jobs import serial_com

# scheduler = BackgroundScheduler(
#     jobstores={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')})
# scheduler.start()
# scheduler.add_job(generate_lecture_history, id="generate_lecture_history", replace_existing=True, trigger="interval", minutes=5)
# scheduler.add_job(generate_payments, id="generate_payments", replace_existing=True, trigger="interval", minutes=1)
