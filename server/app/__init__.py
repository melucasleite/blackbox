# encoding=utf-8
import flask_sqlalchemy
import flask_migrate
import logging
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_restful import Api

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
CORS(app)
from app.models import *
from app.resources import *

api_errors = {
    'ResourceNotFoundError': {
        'message': "Not found",
        'status': 404
    },
    'AccessNotPermittedError': {
        'message': "Forbidden",
        'status': 403
    },
    'InvalidRequestError': {
        'message': 'Invalid request',
        'status': 400
    },
}

api_v1_blueprint = Blueprint('api', __name__)

api = Api(
    api_v1_blueprint,
    errors=api_errors,
)

api.add_resource(PidControllerResource, '/pid_controller/<int:id>', '/pid_controller')
api.add_resource(OutputResource, '/output/<int:id>', '/output')
api.add_resource(ReadingResource, '/reading/<int:id>', '/reading')
app.register_blueprint(api_v1_blueprint, url_prefix='/api')
