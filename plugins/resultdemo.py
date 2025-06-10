from plugin_base import Plugin,AnalyzerResult, ResultFrame, parameter, metadata, SampleTime


@metadata(name="ResultDemo", description="Demo Analyzer Result", simple=False)
class ResultDemo(Plugin):
    width = parameter(SampleTime, SampleTime(100))
    offset = parameter(SampleTime, SampleTime(1000))
    result = parameter(AnalyzerResult, AnalyzerResult("ResultDemo"))
    count = parameter(int, 1)
    def execute(self):
        frame=ResultFrame()
        for i in range(self.count):
            frame.s=self.offset.sample + self.width.sample * i  
            frame.e=frame.s + self.width.sample//2
            frame.type="Test"
            #frame.data={"a":i,"b":123.456,"c":"hello","d":"VERY LONG STRING VERY LONG STRING  VERY LONG STRING VERY LONG STRING VERY LONG STRING VERY LONG STRING "}
            frame.data={"i":i,"d":"very long string very long string very long string very long string"}
            self.result.add(frame)
        yield "Done"
