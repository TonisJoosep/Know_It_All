class Response(Exception):
    """
    Custom class for handling API responses.
    """

    SUCCESS = 0  # Returned results successfully.
    NO_RESULTS = 1  # Could not return results. ... 
    INVALID_PARAMETER = 2  # Contains an invalid parameter. ...
    TOKEN_NOT_FOUND = 3  # Session Token does not exist.
    TOKEN_EMPTY = 4  # Session Token has returned all possible questions ...
    RATE_LIMIT_EXCEEDED = 5  # Too many requests have occurred. ...

    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code
        self.message = message

    def __str__(self):
        return f"API response: {self.message} (code: {self.code})"