from app.pid.CaseRunAdjuster import CaseRunAdjuster
from app.pid.helpers import exceeded_time, get_current_time


class CaseRunStage:
    def __init__(self, GIC_101, TIC_101, HIC_101):
        self.GIC_adjuster = CaseRunAdjuster(
            GIC_101,
            target=1000,
            delay=60 * 60,
            steps=12,
            adjust=(15000 - 1000) / 12)

        self.TIC_adjuster = CaseRunAdjuster(
            TIC_101,
            target=20,
            delay=60 * 60 * 12,
            steps=6,
            adjust=0.5)

        self.HIC_adjuster = CaseRunAdjuster(
            HIC_101,
            target=98,
            delay=60 * 60,
            steps=12,
            adjust=(98 - 55) / 12)

    runtime = 60 * 60 * 24 * 26
    start_time = None

    def stop_conditions(self):
        return not exceeded_time(self.start_time, self.runtime)

    def blocking_loop(self):
        self.start_time = get_current_time()
        while not self.stop_conditions():
            self.loop()

    def loop(self):
        self.GIC_adjuster.loop()
        self.TIC_adjuster.loop()
        self.HIC_adjuster.loop()
