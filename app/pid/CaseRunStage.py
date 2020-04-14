from app.pid.ProportionalAdjuster import ProportionalAdjuster
from app.pid.PIDController import PIDController
from app.pid.helpers import exceeded_time, get_current_time, log


class CaseRunStage:
    def __init__(self, TIC_101: PIDController, GIC_101: PIDController, HIC_101: PIDController):
        self.TIC_101 = TIC_101
        self.GIC_101 = GIC_101
        self.HIC_101 = HIC_101
        self.start_time = None
        self.runtime = 60 * 60 * 24 * 8
        self.update_frequency = 1
        self.last_update = None

    def reached_stop_conditions(self):
        response = exceeded_time(self.start_time, self.runtime)
        return response

    def loop(self):
        log("Case Run Stage Loop", "debug")
        if exceeded_time(self.last_update, self.update_frequency):
            self.last_update = get_current_time()
            self.TIC_101.loop()
            self.GIC_101.loop()
            self.HIC_101.loop()

    def blocking_loop(self):
        log("Case Run Stage Start", "info")
        self.start_time = get_current_time()
        self.last_update = get_current_time()
        while not self.reached_stop_conditions():
            self.loop()
        log("Case Run Stage End", "info")

    # Maintain for 8 days
