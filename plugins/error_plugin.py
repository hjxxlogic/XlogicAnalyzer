from plugin_base import Plugin, Result, parameter, metadata

@metadata(name="ErrorPlugin", description="Raises RuntimeError when trigger=True", simple=False)
class ErrorPlugin(Plugin):
    """A plugin that raises an error when trigger is True."""
    trigger = parameter(bool, False)

    def execute(self):
        # first yield a start message
        yield Result("start")
        # then raise an error to test exception handling
        if self.trigger:
            raise RuntimeError("Intentional error from ErrorPlugin")
        # if no error, yield end
        yield Result("end")
