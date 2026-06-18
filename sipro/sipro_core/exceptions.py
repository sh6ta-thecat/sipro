class SIPROException(Exception):
    pass

class DatabaseException(SIPROException):
    pass

class InstallationException(SIPROException):
    pass

class SecurityException(SIPROException):
    pass

class IPCException(SIPROException):
    pass