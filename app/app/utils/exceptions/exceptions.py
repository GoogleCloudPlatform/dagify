class ValidationError(Exception):
    def __init__(self, msg):
        self.msg = msg


class NotImplementedError(Exception):
    def __init__(
            self,
            msg="method, function or feature is not yet implemented; raise/open an issue on github"):
        self.msg = msg
