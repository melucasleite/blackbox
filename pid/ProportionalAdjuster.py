from pid.PIDController import PIDController
from pid.helpers import get_current_time


class ProportionalAdjuster:
    def __init__(self, controller: PIDController, target, delay, steps, adjust):
        self.controller = controller
        self.target = target
        self.delay = delay
        self.steps = steps
        self.adjust = adjust
        self.step = 1
        self.last_update = None
        self.running = True

    def loop(self):
        if self.running:
            if self.is_first_run():
                self.update()
            elif self.delay_has_passed() and not self.is_last_step():
                self.update()
            elif self.is_last_step():
                self.last_step()

    def update(self):
        self.last_update = get_current_time()
        self.step += 1
        new_setpoint = round(self.controller.get_setpoint() + self.adjust)
        self.controller.set_setpoint(new_setpoint)

    def is_first_run(self):
        return self.last_update is None

    def delay_has_passed(self):
        return (get_current_time() - self.last_update) > self.delay

    def is_last_step(self):
        return self.step == self.steps

    def last_step(self):
        self.controller.set_setpoint(self.target)
        self.running = False
