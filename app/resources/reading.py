from flask import request
from flask_restful import Resource
from app.controllers import reading as controller


class ReadingResource(Resource):
    def get(self, port=None):
        args = request.args
        port = args.get("port")
        interval = args.get("interval")
        limit = int(args.get("limit", 50))
        if not interval:
            readings = controller.retrieve(port, limit)
        else:
            interval = int(interval)
            readings = controller.retrieve_every_n(port, interval, limit)
        return {
            "readings": readings
        }
