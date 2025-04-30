from plugin_base import Plugin, Result, parameter, metadata, SampleTime, Analyzer,Frame


@metadata(name="FrameLog", description="Log Table Text", simple=False)
class FrameLog(Plugin):
    start = parameter(SampleTime, SampleTime(0))
    end = parameter(SampleTime, SampleTime(1000))
    analyzer = parameter(Analyzer, Analyzer(0))
    pattern = parameter(str, "")

    def execute(self):
        frame = Frame(
            self.start.sample, self.end.sample, self.analyzer)
        with open("framelog.log", "w") as f:
            n = 0
            print(self.analyzer.typename,file=f)
            print(self.analyzer.fieldname,file=f)
            print(type(frame),file=f)
            print(dir(frame),file=f)
            while frame.next():
                print(f"{n=}:{frame.s},{frame.e},{frame.type} {frame.data}", file=f)
                n += 1
            yield Result(f"{n}")
