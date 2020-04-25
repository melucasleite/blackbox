from app import db, app
from app.utils.serial_interface import ArduinoSerialInterface

def start_serial_com():
    with app.app_context():
        db.session.flush()
        arduino = ArduinoSerialInterface(interval=1)
        arduino.start()
