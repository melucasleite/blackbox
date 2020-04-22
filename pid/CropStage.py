from pid.ProportionalAdjuster import ProportionalAdjuster
from pid.PIDController import PIDController
from pid.helpers import exceeded_time, log, get_current_time


class CropStage:
    def __init__(self, TIC_101: PIDController, GIC_101: PIDController, HIC_101: PIDController):
        self.GIC_adjuster = ProportionalAdjuster(
            GIC_101,
            target=1000,
            delay=60 * 60,
            steps=12,
            adjust=-(15000 - 1000) / 12)

        self.TIC_adjuster = ProportionalAdjuster(
            TIC_101,
            target=20,
            delay=60 * 60 * 12,
            steps=6,
            adjust=-1)

        self.HIC_adjuster = ProportionalAdjuster(
            HIC_101,
            target=98,
            delay=60 * 60,
            steps=12,
            adjust=(98 - 55) / 12)

    runtime = 60 * 60 * 24 * 26
    start_time = None

    def stop_conditions(self):
        return exceeded_time(self.start_time, self.runtime)

    def blocking_loop(self):
        log("Crop Stage Start", "info")
        self.start_time = get_current_time()
        while not self.stop_conditions():
            self.loop()
        log("Crop Stage End", "info")

    def loop(self):
        log("Crop Stage Loop", "debug")
        self.GIC_adjuster.loop()
        self.TIC_adjuster.loop()
        self.HIC_adjuster.loop()
