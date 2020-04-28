from app import db, app
from app.arduino_interface.arduino_interface import ArduinoInterface
from app.arduino_interface.serial_interface import SerialInterface

def start_serial_com():
    with app.app_context():
        db.session.flush()
        port = SerialInterface(manufacturer="Arduino")
        arduino = ArduinoInterface(port=port)
        arduino.start()
