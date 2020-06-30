from flask import request
from app.controllers import pid_controller
from flask_restful import Resource


class PidControllerResource(Resource):
    def get(self, id=None):
        if id:
            controller = pid_controller.retrieve(id)
            return {"controller": controller.to_dict()}
        else:
            controllers = pid_controller.retrieve_all()
            return {
                "controllers": [x.to_dict() for x in controllers]
            }

    def post(self):
        args = request.json
        name = args.get("name")
        controller = pid_controller.create(name)
        return {"controller": controller.to_dict()}

    def put(self):
        args = request.json
        id = args.get("id")
        name = args.get("name")
        P = args.get("P")
        I = args.get("I")
        D = args.get("D")
        controller = pid_controller.retrieve(id)
        pid_controller.update(controller, name, P, I, D)
        return {"controller": controller.to_dict()}

    def delete(self):
        args = request.json
        id = args.get("id")
        controller = pid_controller.retrieve(id)
        pid_controller.delete(controller)
        return {"message": "Controller deleted."}
