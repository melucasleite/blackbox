# encoding: utf-8
from datetime import datetime
from app import db


class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    port = db.Column(db.String(20))
    reading = db.Column(db.Integer)

    def __init__(self, port, reading):
        self.port = port
        self.reading = reading
        self.deleted = False
        self.created_at = datetime.utcnow()

    def to_short_dict(self):
        return {
            "reading": self.reading,
            "createdAt": self.created_at.isoformat(),
        }

    def to_dict(self):
        return {
            "port": self.port,
            "reading": self.reading,
            "deleted": self.deleted,
            "createdAt": self.created_at.isoformat(),
        }
