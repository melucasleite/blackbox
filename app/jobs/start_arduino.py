import os
import time

from app import db, app
from app.arduino_interface.arduino_interface import ArduinoInterface
from app.arduino_interface.mock_interface import MockInterface
from app.arduino_interface.serial_interface import SerialInterface


def start_arduino():
    with app.app_context():
        db.session.flush()
        if os.environ.get("MOCK_INTERFACE", False):
            port = MockInterface()
        else:
            port = SerialInterface(manufacturer="Arduino")
        arduino = ArduinoInterface(port=port)
        arduino.port.connect()
        time_wait(1)
        while True:
            if arduino.passed_time(arduino.last_read, arduino.interval):
                arduino.last_read = get_time()
                readings = arduino.get_analogs()
                arduino.store_readings(readings)


def get_time():
    return time.time()


def time_wait(duration):
    time.sleep(duration)
