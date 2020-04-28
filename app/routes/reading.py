from flask import request, abort
from app.controllers import reading as controller
from app import app


@app.route("/reading")
def get_reading():
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
