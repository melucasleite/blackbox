# encoding: utf-8
from datetime import datetime

from app import db

controller_modes = ('Manual', 'Auto', 'Master')
units = ['F', 'C', 'PPM', 'percent', '']


class PidController(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)

    name = db.Column(db.String(180))
    P = db.Column(db.DECIMAL(10, 2), nullable=True)
    I = db.Column(db.DECIMAL(10, 2), nullable=True)
    D = db.Column(db.DECIMAL(10, 2), nullable=True)
    mode = db.Column(db.Enum(*controller_modes))
    unit = db.Column(db.Enum(*units))

    output_port = db.Column(db.String(150))
    input_port = db.Column(db.String(150))

    def __init__(self, name, P=1, I=1, D=1, output_port=None, input_port=None, unit=''):
        self.name = name
        self.P = P
        self.I = I
        self.D = D,
        self.output_port = output_port
        self.input_port = input_port
        self.deleted = False
        self.created_at = datetime.utcnow()
        self.unit = unit

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "P": float(self.P),
            "I": float(self.I),
            "D": float(self.D),
            "outputPort": self.output_port,
            "inputPort": self.input_port,
            "deleted": self.deleted,
            "createdAt": self.created_at.isoformat(),
            "mode": "Auto",
            "reading": 23.5,
            "outputs": [
                {
                    "port": "D0",
                    "value": 0.25
                }
            ],
            "unit": self.unit,
            "setPoint": 26.2
        }
