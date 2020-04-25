from app import db, app


def start_serial_com():
    from app.utils.serial_interface import ArduinoSerialInterface
    arduino = ArduinoSerialInterface(interval=0.1)
    arduino.start()
