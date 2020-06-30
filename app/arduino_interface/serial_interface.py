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

from app import db
from app.models import Reading


def get_time():
    return time.time()


class SerialInterface:
    device = None
    port = None
    last_read = 0
    serial_timeout = 0.1
    serial_baudrate = 500000
    reconnect_timeout = 60 * 1  # every 1 minute
    value = 255

    def __init__(self, manufacturer=None):
        self.manufacturer = manufacturer

    def connect(self):
        if self.manufacturer:
            self.device = self.find_device_by_manufacturer()
        if self.device:
            self.port = serial.Serial(self.device, self.serial_baudrate, timeout=self.serial_timeout)

    def find_device_by_manufacturer(self):
        ports = list_ports.comports(include_links=False)
        for port in ports:
            if not port.manufacturer:
                continue
            if self.manufacturer in port.manufacturer.split(" "):
                self.logger(f"Found {self.manufacturer} device at {port.device}.")
                return port.device
        self.device = None
        self.logger(f"{self.manufacturer} device not found.")
        return None

    def reconnect(self):
        self.logger("Trying to reconnect.")
        self.connect()
        time.sleep(self.reconnect_timeout)

    def write(self, string):
        try:
            self.port.write(bytes(string, 'utf-8'))
        except:
            self.reconnect()

    def read(self):
        try:
            data = self.port.readline()[:-2]  # the last bit gets rid of the new-line chars
            if data:
                return data.decode()
            else:
                return ""
        except:
            self.reconnect()
        finally:
            return ""

    @staticmethod
    def logger(message):
        print("[SerialInterface] {}".format(message))
