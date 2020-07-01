# encoding: utf-8
from datetime import datetime

from app import db

controller_modes = ('Manual', 'Auto', 'Master')
units = ['F', 'C', 'PPM', 'percent', '']
analog_pins = [f'A{x}' for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
digital_pins = [f'D{x}' for x in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 44, 45, 46]]


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
    reading = db.Column(db.DECIMAL(10, 2), nullable=True)
    output = db.Column(db.DECIMAL(10, 2), nullable=True)
    set_point = db.Column(db.DECIMAL(10, 2), nullable=True)
    input_port = db.Column(db.Enum(*analog_pins))
    output_port = db.Column(db.Enum(*digital_pins))
    output_port2 = db.Column(db.Enum(*digital_pins))

    def __init__(self, name, P=1, I=1, D=1, output=None, output_port=None, output_port2=None, input_port=None,
                 unit=None,
                 mode=None):
        self.name = name
        self.P = P
        self.I = I
        self.D = D,
        self.output_port = output_port
        self.output_port2 = output_port2
        self.input_port = input_port
        self.output = output
        self.deleted = False
        self.created_at = datetime.utcnow()
        if not unit:
            unit = ''
        self.unit = unit
        if not mode:
            mode = 'Master'
        self.mode = mode

    def to_dict(self):
        response = {
            "id": self.id,
            "name": self.name,
            "P": float(self.P),
            "I": float(self.I),
            "D": float(self.D),
            "outputPort": self.output_port,
            "inputPort": self.input_port,
            "deleted": self.deleted,
            "createdAt": self.created_at.isoformat(),
            "mode": self.mode,
            "reading": float(self.reading),
            "outputs": [
                {
                    "port": self.output_port,
                    "value": float(self.output)
                }
            ],
            "unit": self.unit,
            "setPoint": float(self.set_point),
        }
        if self.output_port2:
            response["outputs"].append({
                "port": self.output_port2,
                "value": float(self.output)
            })
        return response
