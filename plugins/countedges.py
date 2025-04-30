from plugin_base import Plugin, Result, parameter, metadata,SampleTime,Channel,ChannelEdges


@metadata(name="CountEdges", description="Counts edges in ranges", simple=False)
class CountEdges(Plugin):
    start   = parameter(SampleTime, SampleTime(0))
    end     = parameter(SampleTime, SampleTime(1000))
    channel = parameter(Channel,Channel(0))
    
    def execute(self):
        edges = ChannelEdges([self.channel], self.start, self.end,self.common_info.unitsize,self.common_info.blocksize)
        with open("edge.log","w") as f:
            n = 0
            while edges.next():
                if edges.edge &( 1<<self.channel.index):
                    n += 1
                print(f"{n=}:{edges.samplenum},{edges.value},{edges.edge}",file=f)
        yield Result(f"{n}")
        
