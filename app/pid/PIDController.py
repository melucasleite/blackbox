from app.pid.PID import PID
from app.pid.helpers import log


class PIDController:
    def __init__(self, _PID: PID, name):
        self.PID = _PID
        self.reading = 1
        self.output = 1
        self.name = name
        self.input_pin = None
        self.output_pin = None

    def loop(self):
        self.update_reading()
        self.update_pid()
        self.update_pwm()

    def update_reading(self):
        # TODO: Actually read an Analog Input
        # write(output_pin, self.output)
        self.reading = 404

    def update_pid(self):
        self.PID.update(self.reading)

    def update_pwm(self):
        self.output = self.PID.output
        # TODO: Actually update a PWM Output

    def set_setpoint(self, setpoint):
        log("[{}] Setpoint = {}".format(self.name, setpoint), "info")
        self.PID.SetPoint = setpoint

    def get_setpoint(self):
        return self.PID.SetPoint
