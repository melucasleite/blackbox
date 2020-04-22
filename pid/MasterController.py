from pid.CropStage import CropStage
from pid.PID import PID
from pid.PIDController import PIDController
from pid.SpawnStage import SpawnStage
from pid.Stage import Stage
from pid.helpers import log


class MasterController:
    # Master
    TIC_101 = PIDController(PID(10, 1, 1), "TIC_101")
    GIC_101 = PIDController(PID(10, 1, 1), "GIC_101")
    HIC_101 = PIDController(PID(10, 1, 1), "HIC_101")

    spawn_stage = SpawnStage(
        TIC_101=TIC_101,
        GIC_101=GIC_101,
        HIC_101=HIC_101,
    )

    spawn_stage2 = Stage(
        "Spawn",
        controllers=[
            TIC_101,
            GIC_101,
            HIC_101
        ],
        max_runtime=60 * 60 * 24,

    )

    case_run_stage = Stage(
        "Case Run",
        controllers=[
            TIC_101,
            GIC_101,
            HIC_101
        ],
        max_runtime=60 * 60 * 24 * 8
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
