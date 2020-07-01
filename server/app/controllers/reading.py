import json

from app import db
from app.models.reading import Reading
from app.utils.fetch_every_nth_record import fetch_every_nth_record


def retrieve(port: int, limit: int):
    readings: [Reading] = Reading.query \
        .filter_by(deleted=False) \
        .order_by(Reading.id.desc()) \
        .limit(limit) \
        .all()
    if port:
        for reading in readings:
            reading.data = [point for point in reading.data if point["pin"] == port]
    return [reading.to_dict() for reading in readings]


def retrieve_every_n(port: int, n: int, limit: int):
    readings = fetch_every_nth_record(db, "reading", n, limit)
    readings = [{
        "createdAt": reading.created_at.isoformat(),
        "data": json.loads(reading.data)
    } for reading in readings]
    if port:
        for reading in readings:
            reading["data"] = [point for point in reading["data"] if point["pin"] == port]
    return readings
