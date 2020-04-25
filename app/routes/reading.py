from flask import request, abort
from app.controllers import reading
from app import app


@app.route("/reading")
def get_reading():
    args = request.args
    port = args.get("port")
    interval = args.get("interval")
    limit = args.get("limit", 50)
    if not interval:
        readings = reading.retrieve(port, limit)
    else:
        readings = reading.retrieve_every_n(port, interval, limit)
    return {
        "readings": [
            {
                "reading": x.reading,
                "createdAt": x.created_at.isoformat(),
            } for x in readings
        ]
    }
