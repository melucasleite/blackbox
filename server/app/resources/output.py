from flask import request
from app.controllers import output as controller
from flask_restful import Resource, abort


class OutputResource(Resource):
    def post(self):
        args = request.json
        port = args.get("port")
        value = args.get("value")
        if port is None or value is None:
            abort(400)
        output = controller.create(port, value)
        return {"output": output}

    def get(self):
        args = request.args
        port = args.get("port")
        output = controller.retrieve(port)
        return {"output": output}
