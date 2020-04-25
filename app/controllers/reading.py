from app.models.reading import Reading


def retrieve(port: int):
    readings: [Reading] = Reading.query\
        .filter_by(deleted=False)\
        .filter_by(port=port)\
        .order_by(Reading.id.desc())\
        .limit(50)\
        .all()
    return readings
