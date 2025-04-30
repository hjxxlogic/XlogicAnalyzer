from plugin_base import Plugin, Result, parameter, metadata, SampleTime, Analyzer, FrameTableText


@metadata(name="TableLog", description="Log Table Text", simple=False)
class TableLog(Plugin):
    start = parameter(SampleTime, SampleTime(0))
    end = parameter(SampleTime, SampleTime(1000))
    analyzer = parameter(Analyzer, Analyzer(0))
    pattern = parameter(str, "")

    def execute(self):
        text = FrameTableText(
            self.start.sample, self.end.sample, self.analyzer)
        with open("tablelog.log", "w") as f:
            n = 0
            while text.next():
                print(f"{n=}:{text.s},{text.e},{text.t}", file=f)
                n += 1
            yield Result(f"{n}")
