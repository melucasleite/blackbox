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

    def __init__(self, interval=1):
        self.interval = interval

    def setup(self):
        self.device = self.find_arduino()
        self.arduino = serial.Serial(self.device, 500000, timeout=.1)

    def loop(self):
        if self.elasped_time(self.interval):
            print(get_time() - self.last_read)
            readings = self.get_readings()
            self.last_read = get_time()
            print(readings)

    def elasped_time(self, interval):
        return (get_time() - self.last_read) > interval

    def get_readings(self):
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

    def start(self):
        self.setup()
        while True:
            self.loop()

    @staticmethod
    def find_arduino():
        ports = list_ports.comports(include_links=False)
        for port in ports:
            if not port.manufacturer:
                continue
            if "Arduino" in port.manufacturer.split(" "):
                print("Found arduino board at {}".format(port.device))
                return port.device
        print("Arduino Board not found.")
        return None
