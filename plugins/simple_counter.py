from plugin_base import Plugin, Result, parameter, metadata
import time

@metadata(name="SimpleCounter", description="Counts numbers with optional prefix", simple=False)
class SimpleCounter(Plugin):
    estr = parameter(str, "")
    start = parameter(int, 0)
    end = parameter(int, 10000)
    step = parameter(int, 1)
    def execute(self):
        for i in range(self.start, self.end + 1, self.step):
            # simulate computation delay
            time.sleep(0.5)
            yield Result(f"{self.estr}{i}")
