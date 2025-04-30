from plugin_base import Plugin, Result, parameter, metadata
import time

@metadata(name="LongerCounter", description="Counts numbers with longer delay", simple=False)
class LongerCounter(Plugin):
    """A plugin that emits numbers with a 1s delay each."""
    estr = parameter(str, "")
    start = parameter(int, 0)
    end = parameter(int, 0)
    step = parameter(int, 1)

    def execute(self):
        for i in range(self.start, self.end + 1, self.step):
            # simulate longer delay
            time.sleep(1)
            yield Result(f"{self.estr}{i}")
