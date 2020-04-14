from app.pid.PID import PID


class PIDController:
    def __init__(self, _PID: PID):
        self.PID = _PID
        self.reading = 1
        self.output = 1

    def loop(self):
        self.update_reading()
        self.update_pid()
        self.update_pwm()

    def update_reading(self):
        # TODO: Actually read an Analog Input
        self.reading = 404

    def update_pid(self):
        self.PID.update(self.reading)

    def update_pwm(self):
        self.output = self.PID.output
        # TODO: Actually update a PWM Output

    def set_setpoint(self, setpoint):
        self.PID.SetPoint = setpoint

    def get_setpoint(self):
        return self.PID.SetPoint
