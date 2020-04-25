from typing import List

from pid.PIDController import PIDController
from pid.helpers import exceeded_time, get_current_time, log


class Stage:
    def __init__(self,
                 name,
                 controllers: List[PIDController],
                 max_runtime=None,
                 stop_conditions=[],
                 update_frequency=1
                 ):
        self.name = name
        self.controllers = controllers
        self.max_runtime = max_runtime
        self.update_frequency = update_frequency

        # Internal control Vars
        self.start_time = None
        self.last_update = None

    def reached_stop_conditions(self):
        response = False
        if self.max_runtime:
            response = exceeded_time(self.start_time, self.max_runtime)
        return response

    def loop(self):
        log("{} Stage Loop".format(self.name), "debug")
        if exceeded_time(self.last_update, self.update_frequency):
            self.last_update = get_current_time()
            for controller in self.controllers:
                controller.loop()

    def blocking_loop(self):
        log("{} Stage Start".format(self.name), "info")
        self.start_time = get_current_time()
        self.last_update = get_current_time()
        while not self.reached_stop_conditions():
            self.loop()
        log("{} Stage End".format(self.name), "info")
