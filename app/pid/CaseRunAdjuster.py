import time

from app.pid.helpers import get_current_time


class CaseRunAdjuster:
    def __init__(self, controller, target, delay, steps, adjust):
        self.controller = controller
        self.target = target
        self.delay = delay
        self.steps = steps
        self.adjust = adjust
        self.step = 1
        self.last_update = None

    def loop(self):
        if self.is_first_run():
            self.update()
        elif self.delay_has_passed() and not self.is_last_step():
            self.update()
        elif self.is_last_step():
            self.set_setpoint(self.target)

    def update(self):
        self.last_update = get_current_time()
        self.step += 1
        new_setpoint = self.get_setpoint() + self.adjust
        self.set_setpoint(new_setpoint)

    def is_first_run(self):
        return self.last_update is None

    def delay_has_passed(self):
        return (get_current_time() - self.last_update) > self.delay

    def is_last_step(self):
        return self.step == self.steps

    # Boundary methods
    def set_setpoint(self, setpoint):
        self.controller.SetPoint = setpoint

    def get_setpoint(self):
        return self.controller.SetPoint
