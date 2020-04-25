from flask import request, abort
from app.controllers import reading
from app import app


@app.route("/reading")
def get_reading():
    args = request.args
    port = args.get("port")
    interval = args.get("interval")
    if not interval:
        readings = reading.retrieve(port)
    else:
        readings = reading.retrieve_every_n(port, interval)
    return {
        "readings": [
            {
                "reading": x.reading,
                "createdAt": x.created_at.isoformat(),
            } for x in readings
        ]
    }
