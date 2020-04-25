from app import db
from app.models.reading import Reading
from app.utils.fetch_every_nth_record import fetch_every_nth_record


def retrieve(port: int):
    readings: [Reading] = Reading.query \
        .filter_by(deleted=False) \
        .filter_by(port=port) \
        .order_by(Reading.id.desc()) \
        .limit(50) \
        .all()
    return readings


def retrieve_every_n(port: int, n: int):
    records = fetch_every_nth_record("reading", n, db, f"where port={port}")
    return records
