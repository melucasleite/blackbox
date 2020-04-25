from flask import request, abort
from app.controllers import reading
from app import app


@app.route("/reading")
def get_reading():
    args = request.args
    port = args.get("port")
    readings = reading.retrieve(port)
    return {"readings": [x.to_short_dict() for x in readings]}
