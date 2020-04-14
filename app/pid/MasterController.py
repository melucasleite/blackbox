import time

from app.pid.CaseRunStage import CaseRunStage
from app.pid.PID import PID
from app.pid.PIDController import PIDController
from app.pid.SpawnStage import SpawnStage


class MasterController:
    # Master
    TIC_101 = PIDController(PID(10, 1, 1))
    GIC_101 = PIDController(PID(10, 1, 1))
    HIC_101 = PIDController(PID(10, 1, 1))

    spawn_stage = SpawnStage(TIC_101=TIC_101, GIC_101=GIC_101, HIC_101=HIC_101)
    case_run_stage = CaseRunStage(TIC_101=TIC_101, GIC_101=GIC_101, HIC_101=HIC_101)

    def run(self):
        print("Spawn stage start")
        self.spawn_stage.blocking_loop()
        print("Case Run stage start")
        self.case_run_stage.blocking_loop()
