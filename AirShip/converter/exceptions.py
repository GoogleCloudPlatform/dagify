class InvalidConverterType(Exception):
    """Raised when an invalid converter type is provided."""
     
    def __init__(self, message="Raised when an invalid converter type is provided"):
        self.message = message
        super().__init__(message)


class DisabledConverterType(Exception): 
    """Raised when a converter type is provided that is currently disabled."""

    def __init__(self, message="Raised when a converter type is provided that is currently disabled"):
        self.message = message
        super().__init__(message)