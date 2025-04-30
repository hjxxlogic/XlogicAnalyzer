from plugin_base import Plugin, Result, result, metadata

@metadata(name="TypedDemoPlugin", description="Demo plugin returns typed results", simple=True)
class TypedDemoPlugin(Plugin):
    """Plugin that yields typed result instances"""
    def execute(self):
        # yield two typed results
        yield TypedDemoResult(code=100, message="typed result 100")
        yield TypedDemoResult(code=200, message="typed result 200")

class TypedDemoResult(Result):
    """Custom Result subclass with typed fields"""
    code = result(int, 0)
    message = result(str, "")
