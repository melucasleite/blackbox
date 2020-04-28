# encoding: utf-8
from datetime import datetime
from app import db


class Reading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    data = db.Column(db.JSON)

    def __init__(self, data):
        self.data = data
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "data": self.data,
            "createdAt": self.created_at.isoformat(),
        }
