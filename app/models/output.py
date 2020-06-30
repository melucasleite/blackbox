from app import db
from datetime import datetime


class Output(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    executed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)
    port = db.Column(db.Integer)
    value = db.Column(db.Integer)

    def __init__(self, port, value):
        self.port = port
        self.value = value
        self.executed = False
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "port": self.port,
            "value": self.value,
            "executed": self.executed,
            "createdAt": self.created_at.isoformat()
        }
