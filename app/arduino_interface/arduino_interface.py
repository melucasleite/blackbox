import time

from app import db
from app.models.reading import Reading

from app.arduino_interface.serial_interface import SerialInterface
from app.utils.output_value import OutputValue


class ArduinoInterface:
    last_read = 0
    interval = 1

    value = 0

    def __init__(self, port: SerialInterface):
        self.port = port

    def get_analogs(self):
        self.port.write("R")
        data = self.port.read()
        readings = []
        for analog_pin_with_value in data.split("A")[1:]:
            analog_pin = analog_pin_with_value.split("R")[0]
            value = analog_pin_with_value.split("R")[1]
            readings.append({"pin": analog_pin, "value": value})
        return readings

    def write_outputs(self, output_values: [OutputValue]):
        command = ""
        for x in output_values:
            command += f"U{x.output}V{x.value}"
        command += "W"
        self.port.write(command)

    def test_write_output(self):
        self.value = 255 if self.value == 0 else 0
        output_values = [
            OutputValue(5, self.value)
        ]
        self.write_outputs(output_values)

    def store_readings(self, readings):
        db.session.add(Reading(readings))
        db.session.commit()

    @staticmethod
    def passed_time(last_timestamp, interval):
        return (get_time() - last_timestamp) > interval

    @staticmethod
    def logger(message):
        print("[ArduinoInterface] {}".format(message))


def get_time():
    return time.time()
