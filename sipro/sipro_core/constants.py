from enum import Enum


class InstallationStatus(str, Enum):
    PENDING = "PROCESANDO"
    SUCCESS = "EXITOSO"
    FAILED = "FALLIDO"
    CANCELLED = "CANCELADO"
