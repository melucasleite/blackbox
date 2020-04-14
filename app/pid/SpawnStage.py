import time

from app.pid.PIDController import PIDController
from app.pid.helpers import exceeded_time, get_current_time, temperature_reached


class SpawnStage:
    def __init__(self, TIC_101: PIDController, GIC_101: PIDController, HIC_101: PIDController):
        self.TIC_101 = TIC_101
        self.GIC_101 = GIC_101
        self.HIC_101 = HIC_101
        self.runtime = 60 * 60 * 24
        self.last_update = None
        self.start_time = None
        self.update_frequency = 1

    def start(self):
        self.TIC_101.set_setpoint(23)
        self.GIC_101.set_setpoint(15000)
        self.HIC_101.set_setpoint(55)
        self.start_time = get_current_time()
        self.last_update = self.start_time

    def reached_stop_conditions(self):
        response = temperature_reached(self.TIC_101.reading, 23) or exceeded_time(self.start_time, self.runtime)
        print(response)
        return response

    def loop(self):
        print("spawn stage loop: " + str(get_current_time()))
        if self.is_first_run():
            self.start()
        if exceeded_time(self.last_update, self.update_frequency):
            self.TIC_101.loop()
            self.GIC_101.loop()
            self.HIC_101.loop()

    def blocking_loop(self):
        if self.is_first_run():
            self.start()
        while not self.reached_stop_conditions():
            self.loop()

    def is_first_run(self):
        return self.last_update is None
