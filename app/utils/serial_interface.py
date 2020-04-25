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


class ArduinoSerialInterface:
    device = None
    arduino = None

    def setup(self):
        self.device = self.find_arduino()
        self.arduino = serial.Serial(self.device, 115200, timeout=.1)

    def loop(self):
        readings = self.get_readings()
        print(readings)
        time.sleep(0.5)

    def get_readings(self):
        self.arduino.write(b"R")
        time.sleep(1)
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
