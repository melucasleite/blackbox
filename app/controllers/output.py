import json

from app import db
from app.models.output import Output


def create(port, value):
    output = Output(port, value)
    db.session.add(output)
    db.session.commit()
    return output.to_dict()


def retrieve(port: int = None, limit: int = 30):
    outputs: [Output]
    outputs = Output.query \
        .order_by(Output.created_at.desc())
    if port:
        outputs = outputs.filter_by(port=port)
    outputs = outputs.limit(limit).all()
    return [output.to_dict() for output in outputs]
