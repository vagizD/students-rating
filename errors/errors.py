class ScriptError(Exception):
    """
    Parent of all errors in a script.
    """
    def __init__(self, message=None):
        self.message = message


class ParsingError(ScriptError):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return "You got a parsing error.\n" + self.message
