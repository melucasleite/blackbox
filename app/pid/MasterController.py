import time

from app.pid.CaseRunStage import CaseRunStage
from app.pid.CropStage import CropStage
from app.pid.PID import PID
from app.pid.PIDController import PIDController
from app.pid.SpawnStage import SpawnStage
from app.pid.helpers import log


class MasterController:
    # Master
    TIC_101 = PIDController(PID(10, 1, 1))
    GIC_101 = PIDController(PID(10, 1, 1))
    HIC_101 = PIDController(PID(10, 1, 1))

    spawn_stage = SpawnStage(
        TIC_101=TIC_101,
        GIC_101=GIC_101,
        HIC_101=HIC_101)

    case_run_stage = CaseRunStage(
        TIC_101=TIC_101,
        GIC_101=GIC_101,
        HIC_101=HIC_101
    )
    crop_stage = CropStage(
        TIC_101=TIC_101,
        GIC_101=GIC_101,
        HIC_101=HIC_101
    )

    def run(self):
        log("Master program started", "info")
        self.spawn_stage.blocking_loop()
        self.case_run_stage.blocking_loop()
        self.crop_stage.blocking_loop()
        log("Master program ended", "info")
