from flask import request, abort
from app.controllers import output as controller

from app import app


@app.route("/output", methods=["POST"])
def post_output():
    args = request.json
    port = args.get("port")
    value = args.get("value")
    if port is None or value is None:
        abort(400)
    output = controller.create(port, value)
    return {"output": output}


@app.route("/output", methods=["GET"])
def get_output():
    args = request.args
    port = args.get("port")
    output = controller.retrieve(port)
    return {"output": output}
