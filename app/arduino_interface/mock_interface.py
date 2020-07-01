import os
from app.arduino_interface.serial_interface import SerialInterface


class MockInterface(SerialInterface):
    buffer = ''
    is_verbose = os.environ.get("VERBOSE_MODE", False)

    def connect(self):
        self.logger("Mock Interface connected.")

    def write(self, string):
        if self.is_verbose:
            self.logger(f'Write {string}')
        if string == "R":
            self.buffer = self.generate_mock_analog_readings()

    def read(self):
        if self.is_verbose:
            self.logger(f'Read {self.buffer}')
        reading = self.buffer
        self.buffer = ''
        return reading

    def generate_mock_analog_readings(self):
        list = [f'A{x}R{100}' for x in range(0, 16)]
        return ''.join(list)

    @staticmethod
    def logger(message):
        print(f'[MockInterface] {message}')
