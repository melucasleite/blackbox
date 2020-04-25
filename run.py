from app.utils.serial_interface import ArduinoSerialInterface

arduino = ArduinoSerialInterface(interval=0.1)
arduino.start()
