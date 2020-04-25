from flask import request, abort
from app.controllers import pid_controller
from app import app


@app.route("/pid_controller")
def get_pid_controller():
    args = request.args
    id = args.get("id")
    if id:
        controller = pid_controller.retrieve(id)

        return {"controller": controller.to_dict()}
    else:
        controllers = pid_controller.retrieve_all()
        return {
            "controllers": [x.to_dict() for x in controllers]
        }


@app.route("/pid_controller", methods=["POST"])
def post_pid_controller():
    args = request.json
    name = args.get("name")
    controller = pid_controller.create(name)
    return {"controller": controller.to_dict()}


@app.route("/pid_controller", methods=["PUT"])
def put_pid_controller():
    args = request.json
    id = args.get("id")
    name = args.get("name")
    P = args.get("P")
    I = args.get("I")
    D = args.get("D")
    controller = pid_controller.retrieve(id)
    pid_controller.update(controller, name, P, I, D)
    return {"controller": controller.to_dict()}


@app.route("/pid_controller", methods=["DELETE"])
def delete_pid_controller():
    args = request.json
    id = args.get("id")
    controller = pid_controller.retrieve(id)
    pid_controller.delete(controller)
    return {"message": "Controller deleted."}
