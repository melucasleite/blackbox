# # from app import app
# #
# # if __name__ == "__main__":
# # 	app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
# from pid.MasterController import MasterController
#
# master_controller = MasterController()
# master_controller.run()
import time

import serial
from serial.tools import list_ports


def get_time():
    return time.time()


class ArduinoSerialInterface:
    device = None
    arduino = None
    last_read = 0
    serial_timeout = 0.1
    serial_baudrate = 500000
    serial_reconnect_timeout = 1

    def __init__(self, interval=1):
        self.interval = interval

    def start(self):
        self.setup()
        while True:
            self.loop()

    def setup(self):
        self.connect_arduino()

    def loop(self):
        try:
            if self.elasped_time(self.last_read, self.interval):
                self.last_read = get_time()
                readings = self.get_readings_from_arduino()
                self.store_readings(readings)
        except:
            self.try_to_reconnect()

    def connect_arduino(self):
        self.device = self.find_arduino()
        self.arduino = serial.Serial(self.device, self.serial_baudrate, timeout=self.serial_timeout)

    def try_to_reconnect(self):
        self.logger("Trying to reconnect...")
        self.connect_arduino()
        time.sleep(self.serial_reconnect_timeout)

    def get_readings_from_arduino(self):
        self.arduino.write(b"R")
        data = self.arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
        if data:
            data = data.decode()
            readings = []
            for analog_pin_with_value in data.split("A")[1:]:
                analog_pin = analog_pin_with_value.split("R")[0]
                value = analog_pin_with_value.split("R")[1]
                readings.append({"pin": analog_pin, "value": value})
            return readings

    def store_readings(self, readings):
        pass

    def find_arduino(self):
        ports = list_ports.comports(include_links=False)
        for port in ports:
            if not port.manufacturer:
                continue
            if "Arduino" in port.manufacturer.split(" "):
                self.logger("Found arduino board at {}".format(port.device))
                return port.device
        self.logger("Arduino Board not found.")
        return None

    @staticmethod
    def logger(message):
        print("[ArduinoSerialInterface] {}".format(message))

    @staticmethod
    def elasped_time(last_timestamp, interval):
        return (get_time() - last_timestamp) > interval
